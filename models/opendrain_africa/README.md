# OpenDrain-Africa

## Overview

OpenDrain-Africa is an open-source GeoAI semantic-segmentation model designed to identify visible open roadside drainage channels from very high-resolution RGB aerial imagery.

The initial geographic focus is Abeokuta, Ogun State, Nigeria, with the longer-term goal of supporting drainage and flood-resilience mapping in additional African cities.

The model is intended for humanitarian mapping, infrastructure assessment, flood preparedness, disaster-risk reduction, and open mapping workflows.

## Intended Use

OpenDrain-Africa is intended to assist human mappers by identifying visible open constructed drainage channels in high-resolution aerial imagery.

Predictions should be reviewed by human mappers before being incorporated into authoritative mapping datasets.

The model is not intended to determine whether a drainage channel is operational, blocked, damaged, hydraulically adequate, or connected to an underground drainage system.

## Target Feature

The target class is:

- background
- open_drain

An open drain is defined as a visibly identifiable constructed drainage channel that can be confirmed directly from aerial imagery.

Covered drainage infrastructure and drainage that cannot be visually confirmed should not be inferred.

## Architecture

The current OpenDrain-Africa baseline uses a scikit-learn logistic-regression classifier applied to RGB pixels for semantic segmentation.

The model receives three-band RGB aerial imagery and predicts a pixel-level segmentation mask for visible open drainage.

The final production architecture and pretrained checkpoint will be documented before submission after baseline model testing and evaluation are completed.

## Input Imagery

The model is designed for very high-resolution three-band RGB GeoTIFF aerial imagery.

Input bands are:

- Red
- Green
- Blue

The fAIr platform provides 256 x 256 imagery chips. Input imagery is normalized during preprocessing before model inference.

## Output

The model initially produces a semantic-segmentation mask.

Post-processing converts the predicted drainage mask into georeferenced GeoJSON Polygon features suitable for open mapping and GIS workflows.

## Training Data

Training data will consist of openly licensed high-resolution aerial imagery paired with human-validated drainage annotations.

Drainage features will be manually digitized and quality checked before use in model training.

Training and validation areas will use a spatial split to reduce geographic leakage between the two datasets.

## Evaluation

The model will be evaluated on a held-out validation area.

Planned evaluation metrics include:

- Intersection over Union for the open_drain class
- Precision
- Recall
- F1 score

Final performance values will be added after model training and validation are complete.

## Geographic Coverage

The initial training and evaluation effort focuses on Nigeria and, where required, additional African urban areas with suitable openly licensed aerial imagery.

Performance outside the training geography should be independently validated before operational use.

## Limitations

Model performance may be reduced by:

- vegetation covering drainage channels
- heavy shadows
- covered drainage systems
- insufficient image resolution
- water features that resemble constructed drainage
- road edges and dark surfaces that resemble drainage
- geographic differences between training and deployment locations
- poor image quality or unusual capture conditions

The model cannot detect infrastructure that is not visible in the input imagery.

## Human Validation

OpenDrain-Africa is intended as an AI-assisted mapping tool rather than a replacement for human validation.

Predicted features should be inspected and corrected by trained mappers before publication or operational use.

## Pretrained Weights

A publicly distributable pretrained checkpoint will be published before the model contribution is submitted for final review.

## Usage

OpenDrain-Africa is intended to run through the HOT fAIr training and inference pipelines.

The model will support fine-tuning on compatible community-generated datasets and inference on RGB aerial imagery through the fAIr platform.

## Citation

Citation information will be added if the final production architecture relies on a published model architecture or pretrained model.

## License

OpenDrain-Africa is released under the Apache License 2.0.

SPDX identifier: Apache-2.0
