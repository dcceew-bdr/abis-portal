# GSQ Geochemistry Portal

This repository contains the backend web API service and the web UI for the GSQ Geochemistry Portal.

A development version of the portal is deployed in AWS using serverless technologies at https://geochem.dev.kurrawong.ai.

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
