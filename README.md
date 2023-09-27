<p align="center">
   <img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/458/medium640/PyLeap_Logo.png?1635954773" alt="nil"/>
</p>

# PyLeap Project Collection
A collection of projects for the [Pyleap app](https://apps.apple.com/us/app/pyleap/id1582204203). 

Here, PyLeap collaborators can add custom projects to Pyleap by updating this repo. 

Collaborators must provide complete projects from the Adafruit Learn System repo that includes, a project name, an image URL for the user interface, url to the project .zip file, url to the project description, and  a list of devices compatible to the the project. 

[Read more about PyLeap here.](https://learn.adafruit.com/pyleap-app)

```swift
let baseURL = "https://adafruit.github.io/pyleap.github.io/pyleapProjects.json"
```
| Field | Type | Notes |
| --- | --- | --- |
| projectName |String| Sets a title for the project.
| projectImage |URL| An Image URL to a primary image for a project. See **Supported Image Formats** below.
| description |String| A brief description of the project.
| bundleLink |URL| URL to the project .zip file
| learnGuideLink |URL| URL to learn guide or addtional project information.
| compatibility |[String]| A list of devices compatible to the the project using board IDs: "circuitplayground_bluefruit" or "clue_nrf52840_express"
| bluetoothCompatible | Bool |
| wifiCompatible | Bool |
## Supported Image Formats
This lists image formats supported directly by iOS. Of these formats, the PNG format is the one most recommended for use in PyLeap. Generally, the image formats that UIKit supports are the same formats supported by the Image I/O framework.

| Format | Filename extensions |
| --- | --- |
| Portable Network Graphic (PNG)| .png
| Tagged Image File Format (TIFF)| .tiff or .tif
| Joint Photographic Experts Group (JPEG)| .jpeg or .jpg
| Graphic Interchange Format (GIF)| .gif
| Windows Bitmap Format (DIB)| .bmp or .BMPf
| Windows Icon Format| .ico
| Windows Cursor| .cur
| XWindow bitmap| .xbm
