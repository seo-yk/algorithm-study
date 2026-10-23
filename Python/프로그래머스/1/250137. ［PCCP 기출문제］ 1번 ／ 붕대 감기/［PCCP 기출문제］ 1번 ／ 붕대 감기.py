def solution(bandage, health, attacks):
    """
    t초 동안 붕대 감으면서 1초마다 x만큼 체력 회복
    t초 연속으로 붕대를 감는 데 성공하면 y의 체력 추가 회복 (최대 체력 고려)
    공격 시 기술 취소, 공격 당하는 순간엔 체력 회복 X
    기술 취소 및 끝나면 붕대감기 재사용, 연속 성공 시간 = 0
    공격 시 피해량 만큼 체력 감소, 0이면 사망(체력 회복 불가)
    return 남은 체력, 죽으면 -1
    """
    ad = {}
    for t, d in attacks:
        ad[t] = d
        
    t, x, y = bandage
    last_attack = attacks[-1][0] + 1
    cur = health
    success = 0
    for time in range(last_attack):
        print(f"== time:{time}, success:{success}, cur:{cur}")
        # 연속 성공 달성
        if success == t:
            cur = min(health, cur + y)
            success = 0
        
        # 몬스터 공격
        if time in ad:
            success = 0
            cur = max(0, cur - ad[time])
        # 체력 회복
        else:
            cur = min(health, cur + x)
            success += 1
        
        print(f" success:{success}, cur:{cur} ==")
        
        if cur == 0:
            return -1
        
    return cur