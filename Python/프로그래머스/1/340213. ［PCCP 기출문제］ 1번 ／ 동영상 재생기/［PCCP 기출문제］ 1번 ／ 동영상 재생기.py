def solution(video_len, pos, op_start, op_end, commands):
        def to_sec(time):
            return (int(time[:2]) * 60) + int(time[3:])

        video_sec = to_sec(video_len)
        pos_sec = to_sec(pos)
        os_sec = to_sec(op_start)
        oe_sec = to_sec(op_end)

        def op_skip(sec):
            if os_sec <= sec <= oe_sec:
                return oe_sec
            return sec

        pos_sec = op_skip(pos_sec)

        for command in commands:
            if command == 'next':
                pos_sec = min(video_sec, pos_sec + 10)
            elif command == 'prev':
                pos_sec = max(0, pos_sec - 10)

            pos_sec = op_skip(pos_sec)

        return f"{pos_sec // 60:02d}:{pos_sec % 60:02d}"