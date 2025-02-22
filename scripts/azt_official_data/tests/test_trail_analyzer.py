"""
Tests for the trail analyzer module.

Uses known coordinates and distances from the ATA website to verify calculations.
"""

import unittest
from pathlib import Path

from ..utils.trail_analyzer import TrailPoint, analyze_segment

class TestTrailAnalyzer(unittest.TestCase):
    """Test cases for trail analysis functionality."""
    
    def setUp(self):
        """Set up test data directory."""
        self.data_dir = Path(__file__).parent.parent / 'data'
        
        # Exact coordinates from passage_03.gpx track
        self.passage_3_start = TrailPoint(
            latitude=31.512880557,
            longitude=-110.558277627,
            description="Passage 3 Start"
        )
        
        # Last point in the passage_03.gpx track
        self.passage_3_end = TrailPoint(
            latitude=31.596019361,
            longitude=-110.724284677,
            description="Passage 3 End"
        )
        
        # Known distance for Passage 3 from ATA website
        self.known_distance = 18.1  # miles
        
    def test_passage_3_analysis(self):
        """Test analysis of Passage 3 using actual trail endpoints."""
        try:
            segment = analyze_segment(
                start=self.passage_3_start,
                end=self.passage_3_end,
                data_dir=self.data_dir
            )
            
            # Verify distance is within 10% of known distance
            self.assertAlmostEqual(
                segment.stats.total_distance_mi,
                self.known_distance,
                delta=self.known_distance * 0.1,
                msg="Distance should be within 10% of known value"
            )
            
            # Verify passage list
            self.assertEqual(
                segment.passages,
                [3],
                "Segment should only include passage 3"
            )
            
            # Verify coordinates
            self.assertEqual(
                segment.start_point.latitude,
                self.passage_3_start.latitude,
                "Start latitude should match"
            )
            self.assertEqual(
                segment.start_point.longitude,
                self.passage_3_start.longitude,
                "Start longitude should match"
            )
            self.assertEqual(
                segment.end_point.latitude,
                self.passage_3_end.latitude,
                "End latitude should match"
            )
            self.assertEqual(
                segment.end_point.longitude,
                self.passage_3_end.longitude,
                "End longitude should match"
            )
            
            # Verify we have elevation data
            self.assertGreater(
                segment.stats.total_gain_ft,
                0,
                "Should have some elevation gain"
            )
            self.assertGreater(
                segment.stats.total_loss_ft,
                0,
                "Should have some elevation loss"
            )
            
        except FileNotFoundError:
            self.skipTest("GPX data files not found. Run data download first.")
    
    def test_point_outside_trail(self):
        """Test handling of points too far from the trail."""
        # Create a point far from the trail
        far_point = TrailPoint(
            latitude=30.0,  # Way south of the trail
            longitude=-110.0,
            description="Far from trail"
        )
        
        # Verify we get an error when trying to analyze a segment with this point
        with self.assertRaises(ValueError) as context:
            analyze_segment(
                start=self.passage_3_start,
                end=far_point,
                data_dir=self.data_dir
            )
            
        self.assertIn(
            "within 0.5 miles of the trail",
            str(context.exception),
            "Should indicate point is too far from trail"
        )

if __name__ == '__main__':
    unittest.main() 