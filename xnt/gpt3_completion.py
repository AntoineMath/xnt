class GPT3_response:
  models = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]
  pricing = {
       "text-davinci-003": 0.0200,
       "text-babbage-001": 0.005,
       "text-curie-001": 0.0020,
       "text-ada-001": 0.0004
  }

  def __init__(self, response):
    self._response = response
    
  @property
  def text(self) -> str: return self._response.choices[0].text

  @property
  def model(self) -> str: return self._response.model

  @property
  def total_cost(self) -> float:
    price_per_1000 = self.pricing[self.model]
    return (self._response.usage.total_tokens / 1000) * price_per_1000

  @property
  def prompt_cost(self) -> float:
    price_per_1000 = self.pricing[self.model]
    return (self._response.usage.prompt_tokens / 1000) * price_per_1000

  @property
  def completion_cost(self) -> float | None:
    if hasattr(self._response.usage, "completion_tokens"):
      price_per_1000 = self.pricing[self.model]
      return (self._response.usage.completion_tokens / 1000) * price_per_1000
    else: return 0.0

  @property
  def cost_details(self) -> dict:
    return {
      "tot_cost": self.total_cost,
      "completion_cost": self.completion_cost,
      "prompt_cost": self.prompt_cost
    }
  
  @property
  def total_tokens(self) -> int:
    return self._response.usage.total_tokens


