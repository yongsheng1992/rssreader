# Rssreader

一个基于web的RSS/ATOM订阅器。因为对于前端不是很熟悉，所以使用Bootstrap4和jQuery开发前端页面。


## To Do List
- [x] Cli处理环境变量

## How

### 处理环境变量

官方文档中使用`FLASK_ENV`来区分当前的环境是开发还是生产环节，这里也根据该变量来加载不同的配置:

```python
app = create_app(os.getenv('FLASK_ENV') or 'development')
```
