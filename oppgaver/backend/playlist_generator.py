from dataclasses import dataclass

from clients.cover_image_generator_client import CoverImageGeneratorClient
from clients.playlist_description_generator_client import PlaylistDescriptionGeneratorClient
import uuid

def image_cover_prompt(tracks: list[str]):
    # 2.3 Forbedre denne prompten slik at den genererer et relevant coverbilde basert på låtene i spillelisten
    return f"""
        Create a detailed and high quality playlist cover image that fits to the theme and feel of the songs in the playlist:
        {tracks}
    """


def description_prompt(tracks: list[str]):
    # 2.3 Forbedre denne prompten slik at den genererer en relevant beskrivelse basert på låtene i spillelisten
    return f"""
        Create a concise and descriptive description of the playlist based on the songs in the playlist:
        {tracks}
    """


class CoverGenerator:
    def __init__(self):
        self.image_generation_client = CoverImageGeneratorClient()

    def generate_cover_image(self, track_names: list[str]):
        prompt = image_cover_prompt(track_names)
        imageUrl = self.image_generation_client.generate_image(prompt)
        return imageUrl
    


class DescriptionGenerator:
    def __init__(self):
        self.description_generation_client = PlaylistDescriptionGeneratorClient()
    
    def generate_description(self, track_names: list[str]):
        prompt = description_prompt(track_names)
        description = self.description_generation_client.generate_description(prompt)
        return description