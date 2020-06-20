import onnxmltools
from onnxmltools.utils.float16_converter import convert_float_to_float16

input_onnx_model = './hfnet_github.onnx'         # fp32 onnx model
output_onnx_model = './hfnet_github_fp16.onnx'   # fp16 onnx model

onnx_model = onnxmltools.utils.load_model(input_onnx_model)

onnx_model = convert_float_to_float16(onnx_model)
# onnx_model.graph.output.pop()
# onnx_model.graph.output.pop()
# onnx_model.graph.output.pop()
onnxmltools.utils.save_model(onnx_model, output_onnx_model)
