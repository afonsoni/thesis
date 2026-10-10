from unittest.mock import patch

import pytest
from pydantic import BaseModel

from src.rag.common import llm_client


class _Answer(BaseModel):
    parties: list


@pytest.mark.unit
@pytest.mark.parametrize("raw", ['{"parties": ["PS"]}', '[{"parties": ["PS"]}]'])
def test_structured_output_accepts_an_object_wrapped_in_a_one_item_array(raw):
    """gemma-4-26b sometimes answers [{...}]; failing on it sent every query to the fallback analysis."""
    with patch.object(llm_client, "generate_text", return_value=raw):
        assert llm_client.generate_structured("p", _Answer).parties == ["PS"]
