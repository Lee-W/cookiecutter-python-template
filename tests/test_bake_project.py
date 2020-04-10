def test_bake_project(cookies):
    result = cookies.bake(extra_context={"project_name": "helloworld"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "helloworld"
    assert result.project.isdir()
