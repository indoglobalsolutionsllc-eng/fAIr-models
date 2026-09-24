"""a trained model predicts open-drain polygons on a toy chip."""

from pathlib import Path

from .test_steps import _split, _train


def test_predict_returns_open_drain_polygons(generate_toy_dataset: dict[str, Path]) -> None:
    from onnxruntime import InferenceSession

    from models.opendrain_africa.pipeline import export_onnx, predict

    onnx_bytes = export_onnx.entrypoint(_train(generate_toy_dataset, _split(generate_toy_dataset)))
    session = InferenceSession(onnx_bytes, providers=["CPUExecutionProvider"])

    result = predict(session, str(generate_toy_dataset["chips"]), {"confidence_threshold": 0.5})

    assert result["type"] == "FeatureCollection"
    assert result["features"]
    assert all(f["properties"]["label"] == "open_drain" for f in result["features"])
