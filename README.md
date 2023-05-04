
# Homer API 🤠
Free API for Jokes, Facts, Questions and more coming soon!

## API Reference

#### Get Joke

```http
  GET /api/joke
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `joke` | `string` | Returns a Joke from the API. |

#### Get Darkjoke

```http
  GET /api/darkjoke
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `darkjoke` | `string` | Returns a Dark-Joke from the API. |

#### Get Fact

```http
  GET /api/fact
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `fact` | `string` | Returns a Fact from the API. |

#### Get Question

```http
  GET /api/question
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `question` | `string` | Returns a Question from the API. |


## Usage/Examples

```python
import requests

url = requests.get("https://homer-api.up.railway.app/api/darkjoke")
result = url.json()

buildup = result['buildup']
punchline = result['punchline']
joke = buildup + "? " + punchline
print(joke)
```

## Output:
```json
Why did the blind man fall into the well? Because he couldn't see that well.
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

