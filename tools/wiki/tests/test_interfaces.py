import asyncio
import json

from fastmcp import Client

from wiki_tool.cli import main


def test_cli_lint_json_and_strict(wiki, capsys):
    (wiki / "topic.md").write_text("undated\n")
    assert main(["lint", str(wiki), "--json"]) == 0
    assert json.loads(capsys.readouterr().out)["findings"]
    assert main(["lint", str(wiki), "--strict"]) == 1
    assert "undated-page" in capsys.readouterr().out


def test_cli_search_stub(capsys):
    assert main(["search"]) == 0
    assert capsys.readouterr().out.strip() == "not available yet"


def test_mcp_module_imports_lists_four_tools_and_calls_shared_lint(wiki):
    from wiki_tool.server import mcp

    async def check():
        async with Client(mcp) as client:
            tools = await client.list_tools()
            assert {tool.name for tool in tools} == {
                "wiki_lint", "wiki_log", "wiki_rotate", "wiki_merge_logs"
            }
            result = await client.call_tool("wiki_lint", {"wiki": str(wiki)})
            assert not result.is_error

    asyncio.run(check())
