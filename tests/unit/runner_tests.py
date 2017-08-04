from parallel_ci_runner.runner import CIRunner, logger, subprocess, CommandStep

from mock import patch
from unittest import TestCase


class RunnerTests(TestCase):
    """ Test some of the easily unit-testable methods on CIRunner and
    other runners. The integration test provides an end-to-end test.
    """
    def test_add_command_steps(self):
        r = CIRunner()
        r.add_serial_command_step('foo')
        r.add_parallel_command_step(['bar'])
        r.add_parallel_command_step(['one', 'two', 'three'])
        self.assertEqual(r.command_steps, [['foo'], ['bar'], ['one', 'two', 'three']])


class CommandStepTests(TestCase):

    def test_command_is_a_list_with_optional_num_parallel_workers_arg(self):
        command_step = CommandStep([1, 2, 3], num_parallel_workers=2, timeout=20)
        self.assertEqual(list(command_step), [1, 2, 3])
        self.assertEqual(command_step.num_parallel_workers, 2)
        self.assertEqual(command_step.timeout, 20)

    def test_command_step_defaults_parallel_workers_to_commands_length(self):
        command_step = CommandStep([1, 2, 3])
        self.assertEqual(command_step.num_parallel_workers, 3)
