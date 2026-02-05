# Parent Class 1: Camera
class Camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print(f"Camera Quality: {self.camera_quality}")


# Parent Class 2: MusicPlayer
class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print(f"Sound Quality: {self.sound_quality}")


# Child Class: SmartPhone
class SmartPhone(Camera, MusicPlayer):
    def __init__(self, brand, camera_quality, sound_quality):
        # Initialize both parent classes
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)
        self.brand = brand

    def display_smartphone_details(self):
        print(f"Smartphone Brand: {self.brand}")
        # Call parent methods to display details
        self.display_camera_details()
        self.display_music_details()


# Create one object of SmartPhone and display all details
phone = SmartPhone("Samsung Galaxy S24", "108MP Ultra HD", "Dolby Atmos Stereo")
phone.display_smartphone_details()
