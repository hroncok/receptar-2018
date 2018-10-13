import subprocess

def test_run_receptar(project_dir):
    script_path = project_dir / 'receptar.py'
    assert script_path.is_file()
    assert subprocess.check_output(['python3', str(script_path)])
