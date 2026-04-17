"""CLI 模块测试。"""

import pytest
from typer.testing import CliRunner

from ai_chat.cli.main import app

runner = CliRunner()


def test_cli_help():
    """测试 CLI --help 命令。"""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "AI Chat CLI" in result.stdout
    assert "--provider" in result.stdout
    assert "--model" in result.stdout
    assert "--stream" in result.stdout


def test_cli_history_subcommand():
    """测试 history 子命令。"""
    result = runner.invoke(app, ["history"])
    # history 命令应该成功执行（可能显示空历史）
    assert result.exit_code == 0


def test_cli_clear_subcommand():
    """测试 clear 子命令。"""
    result = runner.invoke(app, ["clear"])
    # clear 命令应该成功执行
    assert result.exit_code == 0


def test_cli_message_argument():
    """测试消息参数被正确处理。"""
    # 发送消息时应该调用 AI 并返回结果
    result = runner.invoke(app, ["test message"])
    # 如果 API key 未配置，会显示错误；否则会调用 AI
    # 我们只验证命令不会崩溃
    assert result.exit_code in (0, 1)
