<p align="center">
   <img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/458/medium640/PyLeap_Logo.png?1635954773" alt="nil"/>
</p>

# PyLeap Project Collection
A collection of demo projects for the Pyleap. 

PyLeap is an app for iOS and iPadOS. It allows you to collect complete projects from the Adafruit Learn System repo, and transfer them via Bluetooth to your nRF52840 Bluetooth Low Engery device without use of a code editor.

[Read more about PyLeap here.](https://learn.adafruit.com/pyleap-app)

## Usage
Points to JSON file address.

```swift
let baseURL = "https://github.com/adafruit/pyleap.github.io/blob/gh-pages/pyleapProjects.json"
```
| Field | Type | Notes |
| --- | --- | --- |
| projectName |String| Sets the title of the demo project.
| projectImage |String| URL to the primary image of a demo project in PNG format.
| description |String| A brief description of the demo.
| bundleLink |String| URL to demo project bundle.
| learnGuideLink |String| URL to learn guide in on the Adafruit Learn System.
| compatibility |[String]| An array containing devices bluetooth devices using nRF52840 using FileTransfer.
