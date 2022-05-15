from pybel.page import Page


def test_save(mocker_page_response, tmp_path, page_contents):
	"""Test if a page is saved correctly"""

	# Create a page
	page = Page("0", 1, 1, 1, 1)

	# Save the page
	page.save(tmp_path)
	
	# Check if it saved it correctely
	expected_path = tmp_path / "0-w1-s1-v1-p1.txt"
	assert expected_path.exists()
	assert expected_path.read_text() == '0-w1-s1-v1-p1\n' + page_contents.find(id="textblock").text
