import numpy
from django.core.management import BaseCommand
from sklearn.metrics.pairwise import euclidean_distances
from faces.models import FaceImage, FaceLabelForTest, FaceImageForTest
import pandas as pd
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Check recognition rate'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        face_label_with_parent = FaceLabelForTest.objects.filter(parent__isnull=False)

        min_list = []

        for test_label in tqdm(face_label_with_parent):
            known_images = FaceImage.objects.filter(label=test_label.parent)
            for image in FaceImageForTest.objects.filter(label=test_label):
                distances = [
                    euclidean_distances([image.embedding_array], [face_image.embedding_array])
                    for face_image in known_images
                ]
                min_list.append(numpy.min(distances))

        df = pd.DataFrame(data={'distance': min_list})
        df.to_csv('./closestface.csv')
