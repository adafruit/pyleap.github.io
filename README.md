<p align="center">
   <img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/458/medium640/PyLeap_Logo.png?1635954773" alt="nil"/>
</p>

# PyLeap Project Collection
A collection of demo projects for the Pyleap. 

PyLeap is an app for iOS and iPadOS. It allows you to collect complete projects from the Adafruit Learn System, and transfer them directly to your Circuit Playground Bluefruit without opening a code editor or connecting to a computer.

[Read more about PyLeap here.](https://learn.adafruit.com/pyleap-app)

## Usage
Points to JSON file address.

```swift
let baseURL = "https://adafruit.github.io/pyleap.github.io/PyLeapProjects.json"
```
| Field | Type | Notes |
| --- | --- | --- |
| project_name |String| Sets the title of the demo project |
| project_image |String| URL to the primary image of a demo project in PNG format
| description |String| A brief description of the demo 
| bundle_link |String| URL to demo project bundle 
| learn_guide_link |String| URL to learn guide in on the Adafruit Learn System 
| compatibility |[String]| An array containing devices bluetooth devices using nRF52840 using FileTransfer
