import pathlib
import importlib.util


ROOT = pathlib.Path(__file__).resolve().parent.parent
module_path = ROOT / 'assignments' / 'intro-to-ml-supervised' / 'starter-code.py'
spec = importlib.util.spec_from_file_location('starter', str(module_path))
starter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(starter)


def test_load_data():
    X, y = starter.load_data(str(ROOT / 'assignments' / 'intro-to-ml-supervised' / 'sample_dataset.csv'))
    assert X.shape[0] == y.shape[0]
    assert X.shape[1] == 3


def test_train_and_evaluate():
    X, y = starter.load_data(str(ROOT / 'assignments' / 'intro-to-ml-supervised' / 'sample_dataset.csv'))
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = starter.train_model(X_train, y_train)
    metrics = starter.evaluate(model, X_test, y_test)
    assert 'accuracy' in metrics
    assert 0.0 <= metrics['accuracy'] <= 1.0
    assert metrics['accuracy'] >= 0.6
