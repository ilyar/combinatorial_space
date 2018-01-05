# -*- encoding: utf-8 -*-

import unittest
import numpy as np
from combinatorial_space.minicolumn import Minicolumn, PREDICT_ENUM
from test.unittest.cluster_mock import ClusterMockForPointWeight
from test.unittest.point_mock import PointMockNone, PointMockOddEven, PointMock5Clusters, PointMockInOutCode


class TestMinicolumn__init__(unittest.TestCase):
    def test_space_size(self):
        self.assertRaises(ValueError, Minicolumn, space_size=-10)
        self.assertRaises(ValueError, Minicolumn, space_size=None)

    def test_max_cluster_per_point(self):
        self.assertRaises(ValueError, Minicolumn, max_cluster_per_point=-100)
        self.assertRaises(ValueError, Minicolumn, max_cluster_per_point=None)

    def test_max_count_clusters(self):
        self.assertRaises(ValueError, Minicolumn, max_count_clusters=-1000000)
        self.assertRaises(ValueError, Minicolumn, max_count_clusters=None)

    def test_seed(self):
        self.assertRaises(ValueError, Minicolumn, seed=None)

    def test_threshold_modify(self):
        self.assertRaises(ValueError, Minicolumn, in_threshold_modify=-5)
        self.assertRaises(ValueError, Minicolumn, in_threshold_modify=None)
        self.assertRaises(ValueError, Minicolumn, out_threshold_modify=-5)
        self.assertRaises(ValueError, Minicolumn, out_threshold_modify=None)

    def test_threshold_activate(self):
        self.assertRaises(ValueError, Minicolumn, in_threshold_activate=-5)
        self.assertRaises(ValueError, Minicolumn, in_threshold_activate=None)
        self.assertRaises(ValueError, Minicolumn, out_threshold_activate=-5)
        self.assertRaises(ValueError, Minicolumn, out_threshold_activate=None)

    def test_threshold_bin(self):
        self.assertRaises(ValueError, Minicolumn, threshold_bin=-5)
        self.assertRaises(ValueError, Minicolumn, threshold_bin=None)

    def test_in_out_size(self):
        self.assertRaises(ValueError, Minicolumn, in_random_bits=-5)
        self.assertRaises(ValueError, Minicolumn, out_random_bits=-5)
        self.assertRaises(ValueError, Minicolumn, in_random_bits=None)
        self.assertRaises(ValueError, Minicolumn, out_random_bits=None)

    def test_base_lr(self):
        self.assertRaises(ValueError, Minicolumn, base_lr=-5)
        self.assertRaises(ValueError, Minicolumn, base_lr=None)

    def test_is_modify_lr(self):
        self.assertRaises(ValueError, Minicolumn, is_modify_lr=None)

    def test_count_demensions(self):
        self.assertRaises(ValueError, Minicolumn, count_in_demensions=-5)
        self.assertRaises(ValueError, Minicolumn, count_out_demensions=-5)
        self.assertRaises(ValueError, Minicolumn, count_in_demensions=None)
        self.assertRaises(ValueError, Minicolumn, count_out_demensions=None)

    def test_threshold_bits_controversy(self):
        self.assertRaises(ValueError, Minicolumn, threshold_bits_controversy=-5)
        self.assertRaises(ValueError, Minicolumn, threshold_bits_controversy=None)

    def test_out_non_zero_bits(self):
        self.assertRaises(ValueError, Minicolumn, out_non_zero_bits=-5)
        self.assertRaises(ValueError, Minicolumn, out_non_zero_bits=None)

    def test_class_point(self):
        self.assertRaises(ValueError, Minicolumn, class_point=None)

    def test_size_space(self):
        space_size = 100
        minicolumn = Minicolumn(space_size=space_size, class_point=PointMockNone)
        self.assertEqual(len(minicolumn.space), space_size)

    def test_size_random_bits_count_demensions(self):
        self.assertRaises(ValueError, Minicolumn, in_random_bits=11, count_in_demensions=10)
        self.assertRaises(ValueError, Minicolumn, out_random_bits=11, count_out_demensions=10)

    def test_count_active_point(self):
        self.assertRaises(ValueError, Minicolumn, count_active_point=-1)
        self.assertRaises(ValueError, Minicolumn, count_active_point=None)


class TestPointPredict(unittest.TestCase):
    def setUp(self):
        self.minicolumn_none = Minicolumn(
            space_size=100,
            in_random_bits=1,
            out_random_bits=1,
            count_in_demensions=1,
            count_out_demensions=1,
            class_point=PointMockNone
        )
        self.minicolumn = Minicolumn(
            space_size=20,
            in_random_bits=10,
            out_random_bits=10,
            count_in_demensions=10,
            count_out_demensions=10,
            seed=41,
            threshold_bits_controversy=0.05,
            class_point=PointMockOddEven
        )
        self.minicolumn_front = Minicolumn(
            space_size=20,
            in_random_bits=10,
            out_random_bits=2,
            count_in_demensions=10,
            count_out_demensions=2,
            seed=41,
            threshold_bits_controversy=0.05,
            class_point=PointMockOddEven
        )
        self.minicolumn_back = Minicolumn(
            space_size=20,
            in_random_bits=2,
            out_random_bits=10,
            count_in_demensions=2,
            count_out_demensions=10,
            seed=41,
            threshold_bits_controversy=0.05,
            class_point=PointMockOddEven
        )
        self.minicolumn_out_code = Minicolumn(
            space_size=20,
            in_random_bits=10,
            out_random_bits=2,
            count_in_demensions=10,
            count_out_demensions=2,
            seed=41,
            threshold_bits_controversy=0.05,
            class_point=PointMockInOutCode
        )
        self.minicolumn_in_code = Minicolumn(
            space_size=20,
            in_random_bits=2,
            out_random_bits=10,
            count_in_demensions=2,
            count_out_demensions=10,
            seed=41,
            threshold_bits_controversy=0.05,
            class_point=PointMockInOutCode
        )

    def test_front_assert_not_valid_value(self):
        self.assertRaises(ValueError, self.minicolumn_front.front_predict, [-1] * 10)
        self.assertRaises(ValueError, self.minicolumn_front.front_predict, [2] * 10)
        self.assertRaises(ValueError, self.minicolumn_front.front_predict, [0.8] * 10)
        self.assertRaises(ValueError, self.minicolumn_front.front_predict, None)

    def test_back_assert_not_valid_value(self):
        self.assertRaises(ValueError, self.minicolumn_back.back_predict, [-1] * 10)
        self.assertRaises(ValueError, self.minicolumn_back.back_predict, [2] * 10)
        self.assertRaises(ValueError, self.minicolumn_back.back_predict, [0.8] * 10)
        self.assertRaises(ValueError, self.minicolumn_back.back_predict, None)

    def test_front_assert_not_valid_dem(self):
        self.assertRaises(AssertionError, self.minicolumn_front.front_predict, [1])

    def test_back_assert_not_valid_dem(self):
        self.assertRaises(AssertionError, self.minicolumn_back.back_predict, [1])

    def test_front_assert_not_active_point(self):
        controversy, code, accept = self.minicolumn_none.front_predict([1])
        self.assertEqual(None, code)
        self.assertEqual(None, controversy)
        self.assertEqual(PREDICT_ENUM.THERE_ARE_NOT_ACTIVE_POINTS, accept)

    def test_back_assert_not_active_point(self):
        controversy, code, accept = self.minicolumn_none.back_predict([1])
        self.assertEqual(None, code)
        self.assertEqual(None, controversy)
        self.assertEqual(PREDICT_ENUM.THERE_ARE_NOT_ACTIVE_POINTS, accept)

    def test_front_assert_there_are(self):
        controversy, code, accept = self.minicolumn_none.front_predict([1])
        self.assertEqual(None, code)
        self.assertEqual(None, controversy)
        self.assertEqual(PREDICT_ENUM.THERE_ARE_NOT_ACTIVE_POINTS, accept)

    def test_back_assert_there_are_non_acrive_points(self):
        out_code = [0] + [1] + [1] * 4 + [0] * 4
        controversy, code, accept = self.minicolumn_in_code.back_predict(out_code)

        self.assertEqual(None, code)
        self.assertEqual(None, controversy)
        self.assertEqual(PREDICT_ENUM.THERE_ARE_NONACTIVE_POINTS, accept)

    def test_front_assert_there_are_non_acrive_points(self):
        in_code = [0] + [1] + [1] * 4 + [0] * 4
        controversy, code, accept = self.minicolumn_out_code.front_predict(in_code)

        self.assertEqual(None, code)
        self.assertEqual(None, controversy)
        self.assertEqual(PREDICT_ENUM.THERE_ARE_NONACTIVE_POINTS, accept)

    def test_front_active_point(self):
        controversy, code, accept = self.minicolumn.front_predict([1] * 10)
        np.testing.assert_array_equal(np.array([1, 0, 1, 0, 1, 0, 0, 1, 1, 0]), code)
        self.assertEqual(2, controversy)
        self.assertEqual(PREDICT_ENUM.ACCEPT, accept)

    def test_back_active_point(self):
        controversy, code, accept = self.minicolumn.back_predict([1] * 10)
        np.testing.assert_array_equal(np.array([1, 0, 1, 0, 1, 0, 0, 1, 1, 0]), code)
        self.assertEqual(2, controversy)
        self.assertEqual(PREDICT_ENUM.ACCEPT, accept)


class TestPointSleep(unittest.TestCase):
    def setUp(self):
        self.minicolumn = Minicolumn(
            space_size=5,
            in_random_bits=1,
            out_random_bits=1,
            count_in_demensions=1,
            count_out_demensions=1,
            class_point=PointMock5Clusters
        )
        self.minicolumn_activate = Minicolumn(
            space_size=5,
            in_random_bits=1,
            out_random_bits=1,
            in_threshold_activate=2,
            out_threshold_activate=2,
            count_in_demensions=1,
            count_out_demensions=1,
            class_point=PointMock5Clusters
        )

    def test_assert_input_params(self):
        self.assertRaises(ValueError, self.minicolumn.sleep, threshold_active=2)
        self.assertRaises(ValueError, self.minicolumn.sleep, threshold_active=-1)
        self.assertRaises(ValueError, self.minicolumn.sleep, threshold_in_len=-1)
        self.assertRaises(ValueError, self.minicolumn.sleep, threshold_out_len=-1)
        self.assertRaises(ValueError, self.minicolumn.sleep, threshold_out_len=None)
        self.assertRaises(ValueError, self.minicolumn.sleep, threshold_active=None)
        self.assertRaises(ValueError, self.minicolumn.sleep, threshold_in_len=None)

    def test_no_clusters(self):
        clusters, the_same_clusters = self.minicolumn.sleep()
        self.assertEqual(0, sum([len(cluster) for cluster in clusters]))
        self.assertEqual(0, the_same_clusters)

    def __init_active_mask_less_threshold(self, in_vec, out_vec):
        self.minicolumn_activate.count_clusters = 5 * 5
        for point in self.minicolumn_activate.space:
            for _ in range(5):
                point.clusters.append(ClusterMockForPointWeight(in_vec, out_vec))

    def test_active_out_mask_less_threshold(self):
        self.__init_active_mask_less_threshold(np.array([0, 0, 0, 0, 0]), np.array([1, 1, 1, 1, 1]))
        clusters, the_same_clusters = self.minicolumn_activate.sleep()
        self.assertEqual(0, sum([len(cluster) for cluster in clusters]))
        self.assertEqual(0, the_same_clusters)

    def test_active_in_mask_less_threshold(self):
        self.__init_active_mask_less_threshold(np.array([1, 1, 1, 1, 1]), np.array([0, 0, 0, 0, 0]))
        clusters, the_same_clusters = self.minicolumn_activate.sleep()
        self.assertEqual(0, sum([len(cluster) for cluster in clusters]))
        self.assertEqual(0, the_same_clusters)

    def test_active_mask_more_threshold_all_cluster_active(self):
        self.__init_active_mask_less_threshold(
            np.array([1, 1, 1, 0, 0]),
            np.array([1, 1, 1, 0, 0])
        )

        points, the_same_clusters = self.minicolumn_activate.sleep(threshold_in_len=2, threshold_out_len=2)

        for clusters_number in points:
            np.testing.assert_array_equal([0, 1, 2, 3, 4], clusters_number)

        self.assertEqual(5, sum([len(point.clusters) for point in self.minicolumn_activate.space]))
        self.assertEqual(20, the_same_clusters)

        for point in self.minicolumn_activate.space:
            self.assertEqual(1, len(point.clusters))
            np.testing.assert_array_equal([1, 1, 1, 0, 0], point.clusters[0].in_w)
            np.testing.assert_array_equal([1, 1, 1, 0, 0], point.clusters[0].out_w)

    def test_active_mask_more_threshold_not_all_cluster_active(self):
        self.minicolumn_activate.count_clusters = 5 * 5
        for point in self.minicolumn_activate.space:
            for i in range(5):
                point.clusters.append(ClusterMockForPointWeight(
                    np.array([1] * i + [0] * (5 - i)),
                    np.array([1] * i + [0] * (5 - i))
                ))

        points, the_same_clusters = self.minicolumn_activate.sleep(threshold_in_len=2, threshold_out_len=2)

        for clusters_number in points:
            np.testing.assert_array_equal([3, 4], clusters_number)

        self.assertEqual(10, sum([len(point.clusters) for point in self.minicolumn_activate.space]))
        self.assertEqual(0, the_same_clusters)

        for point in self.minicolumn_activate.space:
            self.assertEqual(2, len(point.clusters))
            np.testing.assert_array_equal([1, 1, 1, 0, 0], point.clusters[0].in_w)
            np.testing.assert_array_equal([1, 1, 1, 1, 0], point.clusters[1].in_w)
            np.testing.assert_array_equal([1, 1, 1, 0, 0], point.clusters[0].out_w)
            np.testing.assert_array_equal([1, 1, 1, 1, 0], point.clusters[1].out_w)


class TestPointUnsupervisedLearningException(unittest.TestCase):
    def setUp(self):
        self.minicolumn = Minicolumn(
            space_size=5,
            in_random_bits=1,
            out_random_bits=1,
            count_in_demensions=1,
            count_out_demensions=1,
            class_point=PointMock5Clusters
        )

    def test_in_codes(self):
        self.assertRaises(ValueError, self.minicolumn.unsupervised_learning, in_codes=None)
        self.assertRaises(ValueError, self.minicolumn.unsupervised_learning, in_codes=np.array([-1]))
        self.assertRaises(ValueError, self.minicolumn.unsupervised_learning, in_codes=np.array([2]))
        self.assertRaises(ValueError, self.minicolumn.unsupervised_learning, in_codes=np.array([0.5]))
        self.assertRaises(ValueError, self.minicolumn.unsupervised_learning, in_codes=np.array([2.5]))
        self.assertRaises(AssertionError, self.minicolumn.unsupervised_learning, in_codes=np.array([1] * 2))

    def test_threshold_controversy_out(self):
        self.assertRaises(ValueError, self.minicolumn.unsupervised_learning, in_codes=np.array([1]),
                          threshold_controversy_out=None)
        self.assertRaises(ValueError, self.minicolumn.unsupervised_learning, in_codes=np.array([1]),
                          threshold_controversy_out=-1)

    def test_threshold_controversy_in(self):
        self.assertRaises(ValueError, self.minicolumn.unsupervised_learning, in_codes=np.array([1]),
                          threshold_controversy_in=None)
        self.assertRaises(ValueError, self.minicolumn.unsupervised_learning, in_codes=np.array([1]),
                          threshold_controversy_in=-1)


if __name__ == '__main__':
    unittest.main()