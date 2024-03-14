from transformers import PegasusTokenizer, PegasusForConditionalGeneration
from torch.cuda import is_available

class TextSummariser: 

    def __init__(self) -> None:
        self._cache_dir: str = '/'.join(__file__.split('/')[:-2]+['models', 'pegasus_cache'])
        self.model_name: str = 'google/pegasus-xsum'
        self.device = 'cuda' if is_available() else 'cpu'
        self.tokenizer = PegasusTokenizer.from_pretrained(self.model_name, cache_dir=self._cache_dir)
        self.model = PegasusForConditionalGeneration.from_pretrained(self.model_name, cache_dir=self._cache_dir).to(self.device)

    def request(self, src_text: str, padding: str = 'max_length', output_length: int = 500) -> str:
        tokens = self.tokenizer.encode(src_text.strip(), truncation=True, padding=padding, return_tensors='pt').to(self.device)
        summary = self.model.generate(tokens ,max_length=output_length, length_penalty=2.6, num_beams=4)
        return self.tokenizer.decode(summary[0], skip_special_tokens=True)

# with open('server/functionalities/text.txt', 'r') as file:
#     text: str = file.read()
#     sum_mod = TextSummariser()
#     answer = sum_mod.request(text, 'max_length', output_length=500)
#     print(answer, len(answer))