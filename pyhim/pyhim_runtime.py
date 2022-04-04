#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main file of pyHiM execution, include the top-level mechanism of pyHiM."""

from run_args import RunArgs
import data_manager
import pipeline

class PyHiMRuntime():
    """pyHiMRuntime class
    """
    def __init__(self):
        """instance of pyhimRuntime object
        """
        pass

if __name__ == "__main__":
    m_run_args = RunArgs()
    m_run_args.parse_args()

    manager = DataManager(m_run_args)
    manager.check_consistency()

    pipe = Pipeline(m_run_args, manager)
    pipe.write()
    pipe.run()
    pass