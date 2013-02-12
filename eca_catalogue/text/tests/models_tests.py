from django.test import TestCase

from eca_catalogue.text.tests.factories import WashingInstructionFactory


class WashingInstructionTest(TestCase):
    def test_model(self):
        obj = WashingInstructionFactory()
        self.assertTrue(obj.pk)

    def test_render_icon(self):
        obj = WashingInstructionFactory()
        self.assertEqual(obj.render_icon(), '<img src="icon.png" alt="text" title="text">')
        obj.icon = None
        self.assertIsNone(obj.render_icon(), None)

