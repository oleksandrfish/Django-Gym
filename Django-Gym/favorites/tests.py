from django.test import TestCase, RequestFactory
from favorites.favorites import (
    get_favorite_barbers,
    get_count_of_favorite_barbers,
    add_barber_to_favorites,
    remove_barber_from_favorites,
    FAVORITE_BARBERS_KEY
)


class FavoritesTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        self.request.session = {}

    def test_get_favorite_barbers_empty(self):
        """Test getting favorite barbers when none exist"""
        result = get_favorite_barbers(self.request)
        self.assertEqual(result, [])

    def test_get_favorite_barbers_with_data(self):
        """Test getting favorite barbers when some exist"""
        self.request.session[FAVORITE_BARBERS_KEY] = [1, 2, 3]
        result = get_favorite_barbers(self.request)
        self.assertEqual(result, [1, 2, 3])

    def test_get_count_of_favorite_barbers_empty(self):
        """Test count when no favorites exist"""
        result = get_count_of_favorite_barbers(self.request)
        self.assertEqual(result, 0)

    def test_get_count_of_favorite_barbers_with_data(self):
        """Test count when favorites exist"""
        self.request.session[FAVORITE_BARBERS_KEY] = [1, 2, 3]
        result = get_count_of_favorite_barbers(self.request)
        self.assertEqual(result, 3)

    def test_add_barber_to_favorites_new(self):
        """Test adding a new barber to favorites"""
        add_barber_to_favorites(self.request, 1)
        result = get_favorite_barbers(self.request)
        self.assertIn(1, result)
        self.assertEqual(len(result), 1)
        # self.assertTrue(self.request.session.modified)

    def test_add_barber_to_favorites_multiple(self):
        """Test adding multiple barbers to favorites"""
        add_barber_to_favorites(self.request, 1)
        add_barber_to_favorites(self.request, 2)
        add_barber_to_favorites(self.request, 3)
        result = get_favorite_barbers(self.request)
        self.assertEqual(result, [1, 2, 3])
        # self.assertTrue(self.request.session.modified)

    def test_add_barber_to_favorites_duplicate(self):
        """Test adding duplicate barber to favorites"""
        add_barber_to_favorites(self.request, 1)
        add_barber_to_favorites(self.request, 1)
        result = get_favorite_barbers(self.request)
        self.assertEqual(result, [1])
        self.assertEqual(len(result), 1)
        # self.assertTrue(self.request.session.modified)

    def test_remove_barber_from_favorites(self):
        """Test removing a barber from favorites"""
        add_barber_to_favorites(self.request, 1)
        add_barber_to_favorites(self.request, 2)
        remove_barber_from_favorites(self.request, 1)
        result = get_favorite_barbers(self.request)
        self.assertNotIn(1, result)
        self.assertIn(2, result)
        self.assertEqual(len(result), 1)
        # self.assertTrue(self.request.session.modified)

    def test_remove_barber_from_favorites_nonexistent(self):
        """Test removing a barber that doesn't exist in favorites"""
        add_barber_to_favorites(self.request, 1)
        remove_barber_from_favorites(self.request, 99)
        result = get_favorite_barbers(self.request)
        self.assertEqual(result, [1])

    def test_remove_all_barbers_from_favorites(self):
        """Test removing all barbers from favorites"""
        add_barber_to_favorites(self.request, 1)
        add_barber_to_favorites(self.request, 2)
        remove_barber_from_favorites(self.request, 1)
        remove_barber_from_favorites(self.request, 2)
        result = get_favorite_barbers(self.request)
        self.assertEqual(result, [])

        