import pandas as pd
from IPython.display import display, HTML

'''HTML/CSS로 스크롤 영역을 만들기
VSCode에서 Jupyter Notebook을 사용하면서 DataFrame 출력이 스크롤 가능한지 여부는 특정 테마나 확장 기능에 따라 다를 수 있습니다. 
아래의의 방법을 사용하면 DataFrame의 출력 결과가 스크롤 가능한 테이블로 변환됩니다.
'''
def display_dataframe(df):
    html = df.to_html(classes='table table-bordered table-striped', escape=False)
    scrollable_html = f"""
        <div style="height: 300px; overflow: auto;">
            {html}
        </div>
    """
    display(HTML(scrollable_html))