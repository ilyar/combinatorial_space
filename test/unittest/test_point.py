# -*- encoding: utf-8 -*-

import unittest
import numpy as np
from src.combinatorial_space.point import Point
from test.unittest import cluster_mock


class TestPoint__init__(unittest.TestCase):
    def test_cluster_class(self):
        self.assertRaises(ValueError, Point, cluster_class=None)

    def test_threshold_modify(self):
        self.assertRaises(ValueError, Point, in_threshold_modify=-1)
        self.assertRaises(ValueError, Point, out_threshold_modify=-1)
        self.assertRaises(ValueError, Point, in_threshold_modify=None)
        self.assertRaises(ValueError, Point, out_threshold_modify=None)

    def test_threshold_activate(self):
        self.assertRaises(ValueError, Point, in_threshold_activate=-1)
        self.assertRaises(ValueError, Point, out_threshold_activate=-1)
        self.assertRaises(ValueError, Point, in_threshold_activate=None)
        self.assertRaises(ValueError, Point, out_threshold_activate=None)

    def test_threshold_bin(self):
        self.assertRaises(ValueError, Point, threshold_bin=-1)
        self.assertRaises(ValueError, Point, threshold_bin=None)

    def test_in_out_size(self):
        self.assertRaises(ValueError, Point, in_random_bits=-1)
        self.assertRaises(ValueError, Point, out_random_bits=-1)
        self.assertRaises(ValueError, Point, in_random_bits=None)
        self.assertRaises(ValueError, Point, out_random_bits=None)

    def test_count_demensions(self):
        self.assertRaises(ValueError, Point, count_out_demensions=-4)
        self.assertRaises(ValueError, Point, count_in_demensions=-4)
        self.assertRaises(ValueError, Point, count_out_demensions=None)
        self.assertRaises(ValueError, Point, count_in_demensions=None)

    def test_base_lr(self):
        self.assertRaises(ValueError, Point, base_lr=-1)
        self.assertRaises(ValueError, Point, base_lr=None)

    def test_max_cluster_per_point(self):
        self.assertRaises(ValueError, Point, max_cluster_per_point=None)
        self.assertRaises(ValueError, Point, max_cluster_per_point=-1)

    def test_is_modify_lr(self):
        self.assertRaises(ValueError, Point, is_modify_lr=None)
        self.assertRaises(ValueError, Point, is_modify_lr=0)


class TestPointBase(unittest.TestCase):
    def setUp(self):
        self.base_point_a = Point(
            in_threshold_modify=1, out_threshold_modify=1,
            in_threshold_activate=1, out_threshold_activate=1,
            threshold_bin=1,
            in_random_bits=1, out_random_bits=1,
            count_in_demensions=1, count_out_demensions=1,
            base_lr=0, is_modify_lr=True,
            max_cluster_per_point=1,
            cluster_class=cluster_mock.ClusterMock0None
        )

        self.base_point_b = Point(
            in_threshold_modify=1, out_threshold_modify=1,
            in_threshold_activate=0, out_threshold_activate=0,
            threshold_bin=1,
            in_random_bits=1, out_random_bits=1,
            count_in_demensions=1, count_out_demensions=1,
            base_lr=0, is_modify_lr=True,
            max_cluster_per_point=1,
            cluster_class=cluster_mock.ClusterMock0None
        )

        self.base_point_c = Point(
            in_threshold_modify=1, out_threshold_modify=1,
            in_threshold_activate=0, out_threshold_activate=0,
            threshold_bin=1,
            in_random_bits=4, out_random_bits=4,
            count_in_demensions=4, count_out_demensions=4,
            base_lr=0, is_modify_lr=True,
            max_cluster_per_point=1,
            cluster_class=cluster_mock.ClusterMock0None
        )

        self.base_point_d0 = Point(
            in_threshold_modify=1, out_threshold_modify=1,
            in_threshold_activate=100, out_threshold_activate=100,
            threshold_bin=1,
            in_random_bits=3, out_random_bits=3,
            count_in_demensions=3, count_out_demensions=3,
            base_lr=0, is_modify_lr=True,
            max_cluster_per_point=5,
            cluster_class=cluster_mock.ClusterMockGetDotCustomBase
        )

        self.base_point_d1 = Point(
            in_threshold_modify=1, out_threshold_modify=1,
            in_threshold_activate=100, out_threshold_activate=0,
            threshold_bin=1,
            in_random_bits=3, out_random_bits=3,
            count_in_demensions=3, count_out_demensions=3,
            base_lr=0, is_modify_lr=True,
            max_cluster_per_point=5,
            cluster_class=cluster_mock.ClusterMockGetDotCustomBase
        )

        self.base_point_d2 = Point(
            in_threshold_modify=1, out_threshold_modify=1,
            in_threshold_activate=0, out_threshold_activate=100,
            threshold_bin=1,
            in_random_bits=3, out_random_bits=3,
            count_in_demensions=3, count_out_demensions=3,
            base_lr=0, is_modify_lr=True,
            max_cluster_per_point=5,
            cluster_class=cluster_mock.ClusterMockGetDotCustomBase
        )

        self.base_point_e = Point(
            in_threshold_modify=1, out_threshold_modify=1,
            in_threshold_activate=0, out_threshold_activate=0,
            threshold_bin=1,
            in_random_bits=3, out_random_bits=3,
            count_in_demensions=3, count_out_demensions=3,
            base_lr=0, is_modify_lr=True,
            max_cluster_per_point=5,
            cluster_class=cluster_mock.ClusterMock1None
        )

        self.base_point_f = Point(
            in_threshold_modify=1, out_threshold_modify=1,
            in_threshold_activate=0, out_threshold_activate=0,
            threshold_bin=1,
            in_random_bits=3, out_random_bits=3,
            count_in_demensions=3, count_out_demensions=3,
            base_lr=0, is_modify_lr=True,
            max_cluster_per_point=5,
            cluster_class=cluster_mock.ClusterMock0None
        )


class TestPointException(TestPointBase):
    def test_less_0_front(self):
        self.assertRaises(ValueError, self.base_point_c.predict_front, [-1] * 1 + [0] * 3)

    def test_less_0_back(self):
        self.assertRaises(ValueError, self.base_point_c.predict_back, [-1] * 1 + [0] * 3)

    def test_not_0_not_1_front(self):
        self.assertRaises(ValueError, self.base_point_c.predict_front, [1] * 1 + [0.2] * 1 + [0] * 2)

    def test_not_0_not_1_back(self):
        self.assertRaises(ValueError, self.base_point_c.predict_back, [1] * 1 + [0] * 1 + [0.2] * 2)

    def test_not_0_not_1_front_2(self):
        self.assertRaises(ValueError, self.base_point_c.predict_front, [-1] * 1 + [0.2] * 1 + [0] * 2)

    def test_not_0_not_1_back_2(self):
        self.assertRaises(ValueError, self.base_point_c.predict_back, [-1] * 1 + [0] * 1 + [0.2] * 2)

    def test_front_type_code_not_valid(self):
        self.assertRaises(ValueError, self.base_point_a.predict_front, [1], 1)

    def test_front_not_activate(self):
        self.assertRaises(AssertionError, self.base_point_a.predict_front, [-1] * 1 + [0] * 9)

    def test_back_type_code_not_valid(self):
        self.assertRaises(ValueError, self.base_point_a.predict_back, [1], 1)

    def test_back_not_activate(self):
        self.assertRaises(AssertionError, self.base_point_a.predict_back, [-1] * 1 + [0] * 9)

    def test_back_dot_less_0(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMockMinusNone(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(ValueError, self.base_point_b.predict_back, [1])

    def test_front_dot_less_0(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMockMinusNone(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(ValueError, self.base_point_b.predict_front, [1])

    def test_back_dot_more_0_out_is_none(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(ValueError, self.base_point_b.predict_back, [1])

    def test_front_dot_more_0_out_is_none(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(ValueError, self.base_point_b.predict_front, [1])

    def test_front_none(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(ValueError, self.base_point_b.predict_front, None)

    def test_back_none(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(ValueError, self.base_point_b.predict_back, None)


class TestPointPredict(TestPointBase):
    def test_back_not_active(self):
        code = [1]
        opt_in_code = self.base_point_a.predict_back(code)
        self.assertEqual([1], code)
        self.assertIsNone(opt_in_code)

    def test_front_not_active(self):
        code = [1]
        opt_in_code = self.base_point_a.predict_front(code)
        self.assertEqual([1], code)
        self.assertIsNone(opt_in_code)

    def test_back_active_empty_cluster(self):
        code = [1]
        opt_in_code = self.base_point_b.predict_back(code)
        self.assertIsNone(opt_in_code)

    def test_front_active_empty_cluster(self):
        code = [1]
        opt_in_code = self.base_point_b.predict_front([1])
        self.assertEqual([1], code)
        self.assertIsNone(opt_in_code)

    def test_back_1_cluster_type_code_0(self):
        self.base_point_c.clusters.append(
            cluster_mock.ClusterMock1CustomBase(
                np.array([1, 1, 0, 0]), np.array([1, 1, 0, 0]), 0, 0, 0, 0, 0)
        )
        code = [1, 0, 0, 0]
        opt_in_code = self.base_point_c.predict_back(code, type_code=0)
        self.assertEqual([1, 0, 0, 0], code)
        np.testing.assert_array_equal([1, 1, 0, 0], opt_in_code)

    def test_front_1_cluster_type_code_0(self):
        self.base_point_c.clusters.append(
            cluster_mock.ClusterMock1CustomBase(
                np.array([1, 1, 0, 0]), np.array([1, 1, 0, 0]), 0, 0, 0, 0, 0)
        )
        code = [1, 0, 0, 0]
        opt_out_code = self.base_point_c.predict_front(code, type_code=0)
        self.assertEqual([1, 0, 0, 0], code)
        np.testing.assert_array_equal([1, 1, 0, 0], opt_out_code)

    def test_back_1_cluster_type_code_minus_1(self):
        self.base_point_c.clusters.append(
            cluster_mock.ClusterMock1CustomBase(
                np.array([1, 1, 0, 0]), np.array([1, 1, 0, 0]), 0, 0, 0, 0, 0)
        )
        code = [1, 0, 0, 0]
        opt_in_code = self.base_point_c.predict_back(code)
        self.assertEqual([1, 0, 0, 0], code)
        np.testing.assert_array_equal([1, 1, -1, -1], opt_in_code)

    def test_front_1_cluster_type_code_minus_1(self):
        self.base_point_c.clusters.append(
            cluster_mock.ClusterMock1CustomBase(
                np.array([1, 1, 0, 0]), np.array([1, 1, 0, 0]), 0, 0, 0, 0, 0)
        )
        code = [1, 0, 0, 0]
        opt_out_code = self.base_point_c.predict_front(code)
        self.assertEqual([1, 0, 0, 0], code)
        np.testing.assert_array_equal([1, 1, -1, -1], opt_out_code)

    def test_back_1_cluster_type_code_0_get_opt_code(self):
        for _ in np.arange(0, 100):
            base_point_d = Point(
                in_threshold_modify=1, out_threshold_modify=1,
                in_threshold_activate=0, out_threshold_activate=0,
                threshold_bin=1,
                in_random_bits=3, out_random_bits=3,
                count_in_demensions=4, count_out_demensions=4,
                base_lr=0, is_modify_lr=True,
                max_cluster_per_point=1,
                cluster_class=cluster_mock.ClusterMock0None
            )
            base_point_d.clusters = [
                cluster_mock.ClusterMock1CustomBase(
                    np.array([1, 1, 1, 0]), np.array([1, 1, 1, 0]), 0, 0, 0, 0, 0)
            ]
            code = [1, 1, 0, 0]
            opt_in_code = base_point_d.predict_back(code)
            self.assertEqual([1, 1, 0, 0], code)
            target = np.array([0, 0, 0, 0])
            target[base_point_d.in_coords] = np.array([1, 1, 1, -1])[base_point_d.in_coords]
            np.testing.assert_array_equal(target, opt_in_code)

    def test_front_1_cluster_type_code_0_get_opt_code(self):
        for _ in np.arange(0, 100):
            base_point_d = Point(
                in_threshold_modify=1, out_threshold_modify=1,
                in_threshold_activate=0, out_threshold_activate=0,
                threshold_bin=1,
                in_random_bits=3, out_random_bits=3,
                count_in_demensions=4, count_out_demensions=4,
                base_lr=0, is_modify_lr=True,
                max_cluster_per_point=1,
                cluster_class=cluster_mock.ClusterMock0None
            )
            base_point_d.clusters = [
                cluster_mock.ClusterMock1CustomBase(
                    np.array([1, 1, 1, 0]), np.array([1, 1, 1, 0]), 0, 0, 0, 0, 0)
            ]
            code = [1, 1, 0, 0]
            opt_out_code = base_point_d.predict_front(code, type_code=0)
            self.assertEqual([1, 1, 0, 0], code)
            target = np.array([0, 0, 0, 0])
            target[base_point_d.out_coords] = np.array([1, 1, 1, 0])[base_point_d.out_coords]
            np.testing.assert_array_equal(target, opt_out_code)

    def test_back_1_cluster_type_code_minus_1_get_opt_code(self):
        for _ in np.arange(0, 100):
            base_point_d = Point(
                in_threshold_modify=1, out_threshold_modify=1,
                in_threshold_activate=0, out_threshold_activate=0,
                threshold_bin=1,
                in_random_bits=3, out_random_bits=3,
                count_in_demensions=4, count_out_demensions=4,
                base_lr=0, is_modify_lr=True,
                max_cluster_per_point=1,
                cluster_class=cluster_mock.ClusterMock0None
            )
            base_point_d.clusters = [
                cluster_mock.ClusterMock1CustomBase(
                    np.array([1, 1, 1, 0]), np.array([1, 1, 1, 0]), 0, 0, 0, 0, 0)
            ]
            code = [1, 1, 0, 0]
            opt_in_code = base_point_d.predict_back(code, type_code=0)
            self.assertEqual([1, 1, 0, 0], code)
            target = np.array([0, 0, 0, 0])
            target[base_point_d.in_coords] = np.array([1, 1, 1, 0])[base_point_d.in_coords]
            np.testing.assert_array_equal(target, opt_in_code)

    def test_front_1_cluster_type_code_minus_1_get_opt_code(self):
        for _ in np.arange(0, 100):
            base_point_d = Point(
                in_threshold_modify=1, out_threshold_modify=1,
                in_threshold_activate=0, out_threshold_activate=0,
                threshold_bin=1,
                in_random_bits=3, out_random_bits=3,
                count_in_demensions=4, count_out_demensions=4,
                base_lr=0, is_modify_lr=True,
                max_cluster_per_point=1,
                cluster_class=cluster_mock.ClusterMock0None
            )
            base_point_d.clusters = [
                cluster_mock.ClusterMock1CustomBase(
                    np.array([1, 1, 1, 0]), np.array([1, 1, 1, 0]), 0, 0, 0, 0, 0)
            ]
            code = [1, 1, 0, 0]
            opt_out_code = base_point_d.predict_front(code)
            self.assertEqual([1, 1, 0, 0], code)
            target = np.array([0, 0, 0, 0])
            target[base_point_d.out_coords] = np.array([1, 1, 1, -1])[base_point_d.out_coords]
            np.testing.assert_array_equal(target, opt_out_code)

    def test_back_get_max_dot_for_opt(self):
        self.base_point_c.clusters = [
            cluster_mock.ClusterMockGetDotCustomBase(
                np.array([1, 1, 0, 0]), np.array([1, 1, 0, 0]), 0, 0, 0, 0, 0),
            cluster_mock.ClusterMockGetDotCustomBase(
                np.array([1, 0, 0, 0]), np.array([1, 0, 0, 0]), 0, 0, 0, 0, 0),
            cluster_mock.ClusterMockGetDotCustomBase(
                np.array([1, 1, 1, 1]), np.array([1, 1, 1, 1]), 0, 0, 0, 0, 0),
            cluster_mock.ClusterMockGetDotCustomBase(
                np.array([1, 1, 0, 1]), np.array([1, 1, 0, 1]), 0, 0, 0, 0, 0)
        ]
        code = [1, 1, 1, 1]
        opt_in_code = self.base_point_c.predict_back(code, 0)
        self.assertEqual([1, 1, 1, 1], code)
        target = np.array([1, 1, 1, 1])
        np.testing.assert_array_equal(target, opt_in_code)

    def test_front_get_max_dot_for_opt(self):
        self.base_point_c.clusters = [
            cluster_mock.ClusterMockGetDotCustomBase(
                np.array([1, 1, 0, 0]), np.array([1, 1, 0, 0]), 0, 0, 0, 0, 0),
            cluster_mock.ClusterMockGetDotCustomBase(
                np.array([1, 0, 0, 0]), np.array([1, 0, 0, 0]), 0, 0, 0, 0, 0),
            cluster_mock.ClusterMockGetDotCustomBase(
                np.array([1, 1, 1, 1]), np.array([1, 1, 1, 1]), 0, 0, 0, 0, 0),
            cluster_mock.ClusterMockGetDotCustomBase(
                np.array([1, 1, 0, 1]), np.array([1, 1, 0, 1]), 0, 0, 0, 0, 0)
        ]
        code = [1, 1, 1, 1]
        opt_out_code = self.base_point_c.predict_front(code, 0)
        self.assertEqual([1, 1, 1, 1], code)
        target = np.array([1, 1, 1, 1])
        np.testing.assert_array_equal(target, opt_out_code)


class TestPointAddExceptions(TestPointBase):

    def test_add_in_none(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(ValueError, self.base_point_b.add, None, np.array([1]))

    def test_add_out_none(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(ValueError, self.base_point_b.add, np.array([1]), None)

    def test_add_in_not_valid_len(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(AssertionError, self.base_point_b.add, np.array([1, 1]), np.array([1]))

    def test_add_out_not_valid_len(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(AssertionError, self.base_point_b.add, np.array([1]), np.array([1, 1]))

    def test_add_in_not_valid_value(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(ValueError, self.base_point_b.add, np.array([-1]), np.array([1]))

    def test_add_out_not_valid_value(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.assertRaises(ValueError, self.base_point_b.add, np.array([1]), np.array([-1]))


class TestPointAdd(TestPointBase):
    def test_add_more_max_clusters(self):
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.base_point_b.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        in_ = np.array([1])
        out_ = np.array([1])
        count_fails, count_modify, is_add = self.base_point_b.add(in_, out_)
        np.testing.assert_array_equal([1], in_)
        np.testing.assert_array_equal([1], out_)
        self.assertEqual(0, count_fails)
        self.assertEqual(0, count_modify)
        self.assertEqual(False, is_add)

    # test_add_new_cluster_* -- проверяют корректность добавления нового кластера, в зависимости от
    # наличия активации входного или выходного вектора

    def test_add_new_cluster_0(self):
        self.base_point_d0.clusters.append(cluster_mock.ClusterMockGetDotCustomBase(0, 0, 0, 0, 0, 0, 0))
        self.base_point_d0.clusters.append(cluster_mock.ClusterMockGetDotCustomBase(0, 0, 0, 0, 0, 0, 0))
        self.base_point_d0.clusters.append(cluster_mock.ClusterMockGetDotCustomBase(0, 0, 0, 0, 0, 0, 0))
        in_ = np.array([1, 0, 0])
        out_ = np.array([1, 0, 0])
        count_fails, count_modify, is_add = self.base_point_d0.add(in_, out_)
        np.testing.assert_array_equal([1, 0, 0], in_)
        np.testing.assert_array_equal([1, 0, 0], out_)
        self.assertEqual(0, count_fails)
        self.assertEqual(0, count_modify)
        self.assertEqual(True, is_add)
        self.assertEqual(len(self.base_point_d0.clusters), 4)

    def test_add_new_cluster_1(self):
        self.base_point_d2.clusters.append(cluster_mock.ClusterMockGetDotCustomBase(0, 0, 0, 0, 0, 0, 0))
        self.base_point_d2.clusters.append(cluster_mock.ClusterMockGetDotCustomBase(0, 0, 0, 0, 0, 0, 0))
        self.base_point_d2.clusters.append(cluster_mock.ClusterMockGetDotCustomBase(0, 0, 0, 0, 0, 0, 0))
        in_ = np.array([1, 0, 0])
        out_ = np.array([1, 0, 0])
        count_fails, count_modify, is_add = self.base_point_d2.add(in_, out_)
        np.testing.assert_array_equal([1, 0, 0], in_)
        np.testing.assert_array_equal([1, 0, 0], out_)
        self.assertEqual(0, count_fails)
        self.assertEqual(0, count_modify)
        self.assertEqual(True, is_add)
        self.assertEqual(len(self.base_point_d2.clusters), 4)

    def test_add_new_cluster_2(self):
        self.base_point_d1.clusters.append(cluster_mock.ClusterMockGetDotCustomBase(0, 0, 0, 0, 0, 0, 0))
        self.base_point_d1.clusters.append(cluster_mock.ClusterMockGetDotCustomBase(0, 0, 0, 0, 0, 0, 0))
        self.base_point_d1.clusters.append(cluster_mock.ClusterMockGetDotCustomBase(0, 0, 0, 0, 0, 0, 0))
        in_ = np.array([1, 0, 0])
        out_ = np.array([1, 0, 0])
        count_fails, count_modify, is_add = self.base_point_d1.add(in_, out_)
        np.testing.assert_array_equal([1, 0, 0], in_)
        np.testing.assert_array_equal([1, 0, 0], out_)
        self.assertEqual(0, count_fails)
        self.assertEqual(0, count_modify)
        self.assertEqual(True, is_add)
        self.assertEqual(len(self.base_point_d1.clusters), 4)

    def test_add_all_clusters_modify(self):
        self.base_point_e.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.base_point_e.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        self.base_point_e.clusters.append(cluster_mock.ClusterMock1None(0, 0, 0, 0, 0, 0, 0))
        in_ = np.array([1, 0, 0])
        out_ = np.array([1, 0, 0])
        count_fails, count_modify, is_add = self.base_point_e.add(in_, out_)
        np.testing.assert_array_equal([1, 0, 0], in_)
        np.testing.assert_array_equal([1, 0, 0], out_)
        self.assertEqual(0, count_fails)
        self.assertEqual(3, count_modify)
        self.assertEqual(False, is_add)
        self.assertEqual(len(self.base_point_e.clusters), 3)

    def test_add_all_clusters_fail(self):
        self.base_point_f.clusters.append(cluster_mock.ClusterMock0None(0, 0, 0, 0, 0, 0, 0))
        self.base_point_f.clusters.append(cluster_mock.ClusterMock0None(0, 0, 0, 0, 0, 0, 0))
        self.base_point_f.clusters.append(cluster_mock.ClusterMock0None(0, 0, 0, 0, 0, 0, 0))
        in_ = np.array([1, 0, 0])
        out_ = np.array([1, 0, 0])
        count_fails, count_modify, is_add = self.base_point_f.add(in_, out_)
        np.testing.assert_array_equal([1, 0, 0], in_)
        np.testing.assert_array_equal([1, 0, 0], out_)
        self.assertEqual(3, count_fails)
        self.assertEqual(0, count_modify)
        self.assertEqual(False, is_add)
        self.assertEqual(len(self.base_point_f.clusters), 3)


if __name__ == '__main__':
    unittest.main()