#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2021 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#
"""Provides an abstract base class for a test generation algorithm."""
from __future__ import annotations

import time
from abc import abstractmethod
from typing import TYPE_CHECKING, Generic, Iterable, List, TypeVar

from ordered_set import OrderedSet

import pynguin.ga.testsuitechromosome as tsc
import pynguin.generation.algorithms.archive as arch

if TYPE_CHECKING:
    import pynguin.coverage.branchgoals as bg
    import pynguin.ga.chromosomefactory as cf
    import pynguin.ga.fitnessfunctions.abstracttestcasefitnessfunction as atcff
    import pynguin.ga.fitnessfunctions.abstracttestsuitefitnessfunction as atsff
    import pynguin.ga.testcasechromosome as tcc
    import pynguin.generation.searchobserver as so
    import pynguin.testcase.testfactory as tf
    from pynguin.ga.operators.crossover.crossover import CrossOverFunction
    from pynguin.ga.operators.ranking.rankingfunction import RankingFunction
    from pynguin.ga.operators.selection.selection import SelectionFunction
    from pynguin.generation.stoppingconditions.stoppingcondition import (
        StoppingCondition,
    )
    from pynguin.setup.testcluster import TestCluster
    from pynguin.testcase.execution.testcaseexecutor import TestCaseExecutor

A = TypeVar("A", bound=arch.Archive)  # pylint:disable=invalid-name


class TestGenerationStrategy(
    Generic[A]
):  # pylint: disable=too-many-instance-attributes,too-many-public-methods
    """Provides an abstract base class for a test generation algorithm."""

    def __init__(self) -> None:
        self._archive: A
        self._chromosome_factory: cf.ChromosomeFactory
        self._executor: TestCaseExecutor
        self._test_cluster: TestCluster
        self._test_factory: tf.TestFactory
        self._selection_function: SelectionFunction
        self._stopping_condition: StoppingCondition
        self._crossover_function: CrossOverFunction
        self._ranking_function: RankingFunction
        self._test_case_fitness_functions: OrderedSet[
            atcff.AbstractTestCaseFitnessFunction
        ] = OrderedSet()
        self._test_suite_fitness_functions: OrderedSet[
            atsff.AbstractTestSuiteFitnessFunction
        ] = OrderedSet()
        self._branch_goal_pool: bg.BranchGoalPool
        self._search_observers: List[so.SearchObserver] = []

    @property
    def chromosome_factory(self) -> cf.ChromosomeFactory:
        """Provides the chromosome factory.

        Returns:
            The chromosome factory
        """
        return self._chromosome_factory

    @chromosome_factory.setter
    def chromosome_factory(self, chromosome_factory):
        self._chromosome_factory = chromosome_factory

    @property
    def executor(self) -> TestCaseExecutor:
        """Provides the test-case executor

        Returns:
            The test-case executor
        """
        return self._executor

    @executor.setter
    def executor(self, executor: TestCaseExecutor) -> None:
        self._executor = executor

    @property
    def test_cluster(self) -> TestCluster:
        """Provide the test cluster.

        Returns:
            The test cluster
        """
        return self._test_cluster

    @test_cluster.setter
    def test_cluster(self, test_cluster: TestCluster) -> None:
        self._test_cluster = test_cluster

    @property
    def test_factory(self) -> tf.TestFactory:
        """Provide the test factory.

        Returns:
            The test factory
        """
        return self._test_factory

    @test_factory.setter
    def test_factory(self, test_factory: tf.TestFactory) -> None:
        self._test_factory = test_factory

    @property
    def archive(self) -> A:
        """Provide the used archive."""
        return self._archive

    @archive.setter
    def archive(self, archive: A) -> None:
        """Set the used archive."""
        self._archive = archive

    @property
    def branch_goal_pool(self) -> bg.BranchGoalPool:
        """Provides the used branch goal pool."""
        return self._branch_goal_pool

    @branch_goal_pool.setter
    def branch_goal_pool(self, branch_goal_pool: bg.BranchGoalPool) -> None:
        """Set the used branch goal."""
        self._branch_goal_pool = branch_goal_pool

    @property
    def selection_function(self) -> SelectionFunction:
        """Provides the used selection function.

        Returns:
            The used selection function
        """
        return self._selection_function

    @selection_function.setter
    def selection_function(self, selection_function: SelectionFunction) -> None:
        self._selection_function = selection_function

    @property
    def stopping_condition(self) -> StoppingCondition:
        """Provides the used stopping condition.

        Returns:
            The used stopping condition
        """
        return self._stopping_condition

    @stopping_condition.setter
    def stopping_condition(self, stopping_condition: StoppingCondition) -> None:
        self._stopping_condition = stopping_condition

    @property
    def crossover_function(self) -> CrossOverFunction:
        """Provides the used crossover function.

        Returns:
            The used crossover function
        """
        return self._crossover_function

    @crossover_function.setter
    def crossover_function(self, crossover_function: CrossOverFunction) -> None:
        self._crossover_function = crossover_function

    @property
    def ranking_function(self) -> RankingFunction:
        """Provides the used ranking function.

        Returns:
            The used ranking function
        """
        return self._ranking_function

    @ranking_function.setter
    def ranking_function(self, ranking_function: RankingFunction):
        self._ranking_function = ranking_function

    @property
    def test_case_fitness_functions(
        self,
    ) -> OrderedSet[atcff.AbstractTestCaseFitnessFunction]:
        """Provides the list of test case fitness functions.

        Returns:
            The used test case fitness functions
        """
        return self._test_case_fitness_functions

    @test_case_fitness_functions.setter
    def test_case_fitness_functions(
        self,
        test_case_fitness_functions: OrderedSet[atcff.AbstractTestCaseFitnessFunction],
    ) -> None:
        self._test_case_fitness_functions = test_case_fitness_functions

    @property
    def test_suite_fitness_functions(
        self,
    ) -> OrderedSet[atsff.AbstractTestSuiteFitnessFunction]:
        """Provides the list of test suite fitness functions.

        Returns:
            The used test suite fitness functions
        """
        return self._test_suite_fitness_functions

    @test_suite_fitness_functions.setter
    def test_suite_fitness_functions(
        self,
        test_suite_fitness_functions: OrderedSet[
            atsff.AbstractTestSuiteFitnessFunction
        ],
    ) -> None:
        self._test_suite_fitness_functions = test_suite_fitness_functions

    def create_test_suite(
        self, population: Iterable[tcc.TestCaseChromosome]
    ) -> tsc.TestSuiteChromosome:
        """Wraps a population of test-case chromosomes in a test-suite chromosome.

        This will add the test suite fitness functions to the resulting chromosome.

        Args:
            population: A list of test-case chromosomes

        Returns:
            A test-suite chromosome
        """
        suite = tsc.TestSuiteChromosome()
        suite.add_test_case_chromosomes(list(population))
        for suite_fitness in self._test_suite_fitness_functions:
            suite.add_fitness_function(suite_fitness)
        return suite

    @abstractmethod
    def generate_tests(self) -> tsc.TestSuiteChromosome:
        """Generates tests for a given module until the time limit is reached.

        Returns:  # noqa: DAR202
            A chromosome containing all tests generated by the generation strategy.
        """

    def add_search_observer(self, observer: so.SearchObserver) -> None:
        """Add the given observer.

        Args:
            observer: The observer to add.
        """
        self._search_observers.append(observer)

    def before_search_start(self) -> None:
        """Has to be called when the search starts."""
        start = time.time_ns()
        for obs in self._search_observers:
            obs.before_search_start(start)

    def before_first_search_iteration(self, initial: tsc.TestSuiteChromosome) -> None:
        """Has to be called once before the very first iteration of the search
        algorithm. Calling this is optional, as not every approach has a result before
        the first iteration.

        Args:
            initial: The initially produced test suite.
        """
        for obs in self._search_observers:
            obs.before_first_search_iteration(initial)

    def after_search_iteration(self, best: tsc.TestSuiteChromosome) -> None:
        """Has to be called after every iteration of the search algorithm.

        Args:
            best: The currently best produced test suite.
        """
        for obs in self._search_observers:
            obs.after_search_iteration(best)

    def after_search_finish(self) -> None:
        """Has to be called when the search has finished."""
        for obs in self._search_observers:
            obs.after_search_finish()

    def resources_left(self) -> bool:
        """Checks if there are still resources left, e.g., time or test case executions.

        Returns:
            Whether or not there are resources left.
        """
        return not self._stopping_condition.is_fulfilled()

    def progress(self) -> float:
        """Provides the progress of the search.

        Returns:
            A value in [0,1]."""
        limit = self._stopping_condition.limit()
        assert limit > 0.0
        return self._stopping_condition.current_value() / limit
