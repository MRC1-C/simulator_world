import pygame
from os import walk

def import_folder(size,path):
    surface_list = []

    for _,__,img_files in walk(path):
        img_files = sorted(img_files)
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf, (size, size))
            surface_list.append(image_surf)

    return surface_list