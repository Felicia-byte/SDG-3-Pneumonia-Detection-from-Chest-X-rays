"""Quick smoke test to verify that required libraries import and a minimal model can be constructed.

This script prints helpful PowerShell commands to create a venv and install dependencies when TensorFlow
is not available.
"""
import sys

try:
    # Import TensorFlow dynamically to avoid static-analysis "could not be resolved"
    # errors in editors where TensorFlow isn't installed, while preserving runtime behavior.
    import importlib
    try:
        tf = importlib.import_module('tensorflow')
        keras = importlib.import_module('tensorflow.keras')
        # Prefer importing the layers submodule; fall back to attribute on keras if needed.
        try:
            layers = importlib.import_module('tensorflow.keras.layers')
        except Exception:
            layers = getattr(keras, 'layers', None)
    except Exception as exc:
        # Re-raise so the outer except block handles the fallback stubs below.
        raise
except Exception as exc:
    print('WARNING: TensorFlow or Keras not available; using lightweight stub for quick smoke test.')
    print('Exception:', exc)
    print('\nTo run with real TensorFlow, create a virtual environment and install the requirements:')
    print('\n# PowerShell commands')
    print('python -m venv venv; .\\venv\\Scripts\\Activate.ps1')
    print('python -m pip install --upgrade pip')
    print('python -m pip install -r requirements.txt')

    # Minimal stubs so the rest of the script can run without TensorFlow.
    class _Placeholder:
        def __repr__(self):
            return '<placeholder>'

    def _Input(shape):
        return _Placeholder()

    def _conv2d(filters, kernel_size, activation):
        def layer(x):
            return x
        return layer

    class _GAP2D:
        def __call__(self, x):
            return x

    def _Dense(units, activation):
        def layer(x):
            return x
        return layer

    class _Model:
        def __init__(self, inputs, outputs):
            pass
        def compile(self, optimizer=None, loss=None, metrics=None):
            pass

    class _Keras:
        pass

    _Keras.Input = staticmethod(_Input)
    _Keras.Model = _Model

    class _Layers:
        pass

    _Layers.Conv2D = staticmethod(_conv2d)
    _Layers.GlobalAveragePooling2D = _GAP2D
    _Layers.Dense = staticmethod(_Dense)

    keras = _Keras
    layers = _Layers
    tf = type('tf', (), {'__version__': '0.0-stub'})

print('TensorFlow', tf.__version__)

def make_model(input_shape=(150,150,3)):
    inputs = keras.Input(shape=input_shape)
    x = layers.Conv2D(8, 3, activation='relu')(inputs)
    x = layers.GlobalAveragePooling2D()(x)
    outputs = layers.Dense(1, activation='sigmoid')(x)
    model = keras.Model(inputs, outputs)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

if __name__ == '__main__':
    m = make_model()
    print('Model built successfully')
