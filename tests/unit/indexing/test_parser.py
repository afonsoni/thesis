from src.rag.indexing.parser import strip_images


def test_strip_images_removes_every_image_form():
    md = (
        "# Saúde\n\n"
        "![](_page_0_Picture_0.jpeg)\n\n"
        "Reforçar o SNS.\n\n"
        "![red star person](https://i.imgur.com/9999999.png)\n\n"
        "![Image of a red star-shaped figure]\n\n"
        "Texto com [uma ligação](https://example.pt) normal.\n"
    )
    assert strip_images(md) == (
        "# Saúde\n\n"
        "Reforçar o SNS.\n\n"
        "Texto com [uma ligação](https://example.pt) normal.\n"
    )
