#딕셔너리는 중괄호
player = {
  'name': 'nico',
  'age':'12',
  'alive': True,
  'fav_food' : ["pizza", "hambuger"]
}
#player라는 딕셔너리에 해당 속성들이 속한다는 개념

print(player.get('age'))

print
#리스트와 다르게 순서가 정해져 있지 않으므로 순서가 아니라 속성을 지정해서 추출할 수 있다.
"""
딕셔너리 데이터 변경방법
1. clear = 전부 삭제
2. pop = remove
player.pop('age')
3. 대괄호 = 새로 추가
player['xp'] = 1500
"""
#키 값으로는 문자열, 참거짓, 숫자, 리스트, 튜플이 사용가능

