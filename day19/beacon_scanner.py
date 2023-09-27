from collections import namedtuple
from typing import List, Tuple, Set, Dict

Beacon = namedtuple("Beacon", "x y z")
Scanner = namedtuple("Scanner", "name beacons")


def parse(lines: List[str]) -> List[Scanner]:
    scanners = []
    current = None

    for line in lines:
        if line.startswith("---"):
            name = line.replace("---", "").strip()
            current = Scanner(name, [])
        elif len(line.strip()) > 0:
            x, y, z = line.split(",")
            current.beacons.append(Beacon(int(x), int(y), int(z)))
        else:
            scanners.append(current)
            current = None
    scanners.append(current)
    return scanners


def _manhattan_distance(left: Beacon, right: Beacon) -> int:
    return abs(left.x - right.x) + abs(left.y - right.y) + abs(left.z - right.z)


def _beacon_distances(idx: int, scanner: Scanner) -> Dict[int, Beacon]:
    base = scanner.beacons[idx]
    distances = {}
    for beacon in scanner.beacons:
        if beacon != base:
            distance = _manhattan_distance(base, beacon)
            distances[distance] = beacon
    return distances


def find_overlaps(scanner: Scanner, other: Scanner) -> List[Tuple[Beacon, Beacon]]:
    for i in range(len(scanner.beacons)):
        scanner_distances = _beacon_distances(i, scanner)
        for j in range(len(other.beacons)):
            other_distances = _beacon_distances(j, other)
            common = set(scanner_distances.keys()).intersection(set(other_distances.keys()))
            if len(common) >= 11:
                return [(scanner_distances[key], other_distances[key]) for key in common]


rotation_functions = (
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-z, -y, -x)
)


def _subtract(left: Beacon, right: Beacon) -> Tuple[int, int, int]:
    return left.x - right.x, left.y - right.y, left.z - right.z


def _add(left: Beacon, right: Beacon) -> Tuple[int, int, int]:
    return left.x + right.x, left.y + right.y, left.z + right.z


def find_position(left: Scanner, right: Scanner, overlapping_beacons: List[Tuple[Beacon, Beacon]]):
    res = [[], [], []]
    i = 0
    for left_beacon, right_beacon in overlapping_beacons[0:2]:
        for idx, rotation_fn in enumerate(rotation_functions):
            distance = _subtract(left_beacon, Beacon(*rotation_fn(right_beacon.x, right_beacon.y, right_beacon.z)))
            res[i].append(distance)
            res[2].append(rotation_fn)
        i += 1
    for i in range(len(res[0])):
        if res[0][i] == res[1][i]:
            scanner_abs_pos = res[0][i]
            return [_add(Beacon(*res[2][i](b.x, b.y, b.z)), Beacon(*res[0][i])) for b in right.beacons], scanner_abs_pos
    return None, None


def solve(scanners: List[Scanner]):
    scanners_dict = {}
    for scanner in scanners:
        scanners_dict[scanner.name] = scanner

    base = scanners[0]

    known = {base.name}
    unknown = set(scanner.name for scanner in scanners[1:])
    scanner_abs_poss = []

    while len(unknown) > 0:
        temp_k = set()
        temp_u = set()
        for k in known:
            for u in unknown:
                left = scanners_dict[k]
                right = scanners_dict[u]
                overlaps = find_overlaps(left, right)
                if overlaps is not None:
                    converted, scanner_abs_pos = find_position(left, right, overlaps)
                    if converted is not None:
                        scanner_abs_poss.append(scanner_abs_pos)
                        temp_k.add(right.name)
                        temp_u.add(right.name)
                        scanners_dict[right.name] = Scanner(right.name, [Beacon(*c) for c in converted])
        for i in temp_k:
            known.add(i)
        for i in temp_u:
            unknown.remove(i)

    all_beacons = set()
    for scanner in scanners_dict.values():
        for beacon in scanner.beacons:
            all_beacons.add(beacon)

    return len(all_beacons), find_max_manhattan_distance(scanner_abs_poss)


def find_max_manhattan_distance(scanner_abs_positions: List[Tuple[int, int, int]]):
    max_distance = 0
    for i in scanner_abs_positions:
        for j in scanner_abs_positions:
            distance = _manhattan_distance(Beacon(*i), Beacon(*j))
            if distance > max_distance:
                max_distance = distance
    return max_distance
