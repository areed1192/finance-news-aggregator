"""Tests for deprecated method aliases across providers."""

import warnings
from unittest.mock import patch

from finnews.cnn_finance import CNNFinance
from finnews.nasdaq import NASDAQ
from finnews.sp_global import SPGlobal


# ---------------------------------------------------------------------------
# Deprecation alias tests
# ---------------------------------------------------------------------------


class TestDeprecationAliases:
    """Tests that old misspelled method names emit DeprecationWarning."""

    def test_cnn_techonology_warns(self):
        """Verify CNNFinance.techonology() warns and delegates to technology()."""
        client = CNNFinance()

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with patch.object(client, "technology", return_value=[]) as mock:
                client.techonology()
                mock.assert_called_once()
            assert len(w) == 1
            assert "deprecated" in str(w[0].message).lower()

    def test_nasdaq_artifical_intelligence_warns(self):
        """Verify NASDAQ.artifical_intelligence_feed() warns and delegates."""
        client = NASDAQ()

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with patch.object(
                client, "artificial_intelligence_feed", return_value=[]
            ) as mock:
                client.artifical_intelligence_feed()
                mock.assert_called_once()
            assert len(w) == 1
            assert "deprecated" in str(w[0].message).lower()

    def test_sp_global_all_indicies_warns(self):
        """Verify SPGlobal.all_indicies() warns and delegates to all_indices()."""
        client = SPGlobal()

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with patch.object(client, "all_indices", return_value=[]) as mock:
                client.all_indicies()
                mock.assert_called_once()
            assert len(w) == 1
            assert "deprecated" in str(w[0].message).lower()

    def test_sp_global_index_announcments_warns(self):
        """Verify SPGlobal.index_announcments() warns and delegates."""
        client = SPGlobal()

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with patch.object(client, "index_announcements", return_value=[]) as mock:
                client.index_announcments()
                mock.assert_called_once()
            assert len(w) == 1
            assert "deprecated" in str(w[0].message).lower()

    def test_sp_global_new_counsultations_warns(self):
        """Verify SPGlobal.new_counsultations() warns and delegates."""
        client = SPGlobal()

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with patch.object(client, "new_consultations", return_value=[]) as mock:
                client.new_counsultations()
                mock.assert_called_once()
            assert len(w) == 1
            assert "deprecated" in str(w[0].message).lower()
