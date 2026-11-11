import numpy as np
import onnxruntime as ort


session = ort.InferenceSession(
    'ml/models/cnn_classifier_v1.onnx',
    providers=['CPUExecutionProvider']
)


img_test=np.random.rand(1,1,128,512).astype(np.float32)

outputs=session.run(
    None,
    {'images': img_test}
)

logits=outputs[0]
prob= 1/(1+np.exp(-logits))
print(prob.item())
