# ABIS Portal

This repository contains the backend web API service and the web UI for the ABIS Portal, a development version of which is online at <https://abis.dev.kurrawong.ai/>.

Future versions of this Portal will not be delivered at the above location.


## Contact

For all matters relating to this Portal, please contact:

**Dr Nicholas Car**  
_Delivery Manager_  
Biodiversity Data Repository Project  
Department of Climate Change, Energy, the Environment and Water  
<nicholas.car@dcceew.gov.au> 

## Technical Details
![AWS Architecture Diagram](static/aws-architecture.svg)

## Building for AWS Lambda

If you're on a Windows or macOS machine, use Docker to build a Debian container to build and create the `lambda.zip` file.

```
task lambda:container:build
```

Once the build is finished, you will be inside the Debian container. Generate the artifact.

```
task lambda:zip
```

Exit the container and now in the `dist/` directory, there should be a `lambda.zip` artifact ready to be uploaded to AWS Lambda.
