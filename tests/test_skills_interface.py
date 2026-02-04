def test_skills_folder_exists():
    # Minimal sanity test: repo structure should include skills folder
    import os
    assert os.path.isdir("skills")
