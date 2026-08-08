import random
import unittest

from agent import ArmStats, AutonomyMode, Event, aggregate, choose_arm, filter_min_conversions, may_publish, report, reward


class MarketingCoreTests(unittest.TestCase):
    def test_duplicate_events_are_idempotent(self):
        stats = aggregate([Event("same", "x", "conversion"), Event("same", "x", "conversion")])
        self.assertEqual(stats["x"].conversions, 1)

    def test_unknown_event_is_rejected(self):
        with self.assertRaises(ValueError):
            aggregate([Event("1", "x", "hallucinated")])

    def test_reward_is_deterministic_and_explainable(self):
        self.assertEqual(reward(ArmStats(impressions=20, clicks=3, conversions=2)), 206.2)

    def test_minimum_conversions_filters_arms_and_counts_them(self):
        kept, filtered = filter_min_conversions({"a": ArmStats(conversions=1), "b": ArmStats(conversions=0)}, 1)
        self.assertEqual(list(kept), ["a"])
        self.assertEqual(filtered, 1)

    def test_report_makes_filtering_visible(self):
        text = report({"a": ArmStats(conversions=0)}, minimum=1)
        self.assertIn("1 arm(s) filtered", text)

    def test_negative_threshold_is_rejected(self):
        with self.assertRaises(ValueError):
            filter_min_conversions({}, -1)

    def test_thompson_selection_is_repeatable_with_seeded_rng(self):
        arms = {"a": ArmStats(impressions=10, conversions=4), "b": ArmStats(impressions=10, conversions=0)}
        self.assertEqual(choose_arm(arms, random.Random(7)), choose_arm(arms, random.Random(7)))

    def test_approval_mode_requires_approval(self):
        self.assertFalse(may_publish(AutonomyMode.APPROVAL, False))
        self.assertTrue(may_publish(AutonomyMode.APPROVAL, True))
        self.assertFalse(may_publish(AutonomyMode.SUGGEST_ONLY, True))
        self.assertTrue(may_publish(AutonomyMode.FULL, False))


if __name__ == "__main__":
    unittest.main()
