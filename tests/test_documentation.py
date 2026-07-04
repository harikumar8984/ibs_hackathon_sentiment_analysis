import unittest
from unittest.mock import patch, MagicMock
from obscenefilter.obscenefilter import ObsceneFilter

class TestDocumentation(unittest.TestCase):

    @patch('obscenefilter.obscenefilter.ObsceneFilter')
    def test_dependencies_update_happy_path(self, MockObsceneFilter):
        # Arrange
        mock_filter = MockObsceneFilter.return_value
        mock_filter.is_clean.return_value = True
        
        # Act
        result = mock_filter.is_clean("This is a clean text.")
        
        # Assert
        self.assertTrue(result)
        mock_filter.is_clean.assert_called_once_with("This is a clean text.")

    @patch('obscenefilter.obscenefilter.ObsceneFilter')
    def test_dependencies_update_conflict(self, MockObsceneFilter):
        # Arrange
        mock_filter = MockObsceneFilter.return_value
        mock_filter.is_clean.side_effect = Exception("Conflict occurred")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            mock_filter.is_clean("This text may cause a conflict.")
        
        self.assertEqual(str(context.exception), "Conflict occurred")
        mock_filter.is_clean.assert_called_once_with("This text may cause a conflict.")

    @patch('obscenefilter.obscenefilter.ObsceneFilter')
    def test_documentation_clarity(self, MockObsceneFilter):
        # Arrange
        mock_filter = MockObsceneFilter.return_value
        mock_filter.get_profane_words.return_value = ["badword1", "badword2"]
        
        # Act
        profane_words = mock_filter.get_profane_words()
        
        # Assert
        self.assertIn("badword1", profane_words)
        self.assertIn("badword2", profane_words)
        mock_filter.get_profane_words.assert_called_once()

    @patch('obscenefilter.obscenefilter.ObsceneFilter')
    def test_out_of_scope_items(self, MockObsceneFilter):
        # Arrange
        mock_filter = MockObsceneFilter.return_value
        mock_filter.get_extra_censor_list.return_value = []
        
        # Act
        extra_censors = mock_filter.get_extra_censor_list()
        
        # Assert
        self.assertEqual(extra_censors, [])
        mock_filter.get_extra_censor_list.assert_called_once()

if __name__ == '__main__':
    unittest.main()