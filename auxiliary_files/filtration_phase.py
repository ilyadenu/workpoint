import cmath


phase_after_fft = [36.12741527700629+1j, 56.00232600194687+1j, 85.52070617854491+1j, 119.91628102948694+1j,
                   155.7904614455971+0j, 192.11413707329223+0j, 228.59041526423945+0j, 265.1210434197672+0j]


def complex_to_phi(complex_number):
    # Получаем угол в радианах с использованием функции phase
    phi_radians = cmath.phase(complex_number)

    # Преобразуем угол в градусы
    phi_degrees = phi_radians * 180 / cmath.pi

    return phi_degrees


phi = complex_to_phi(phase_after_fft[3])
print(phi)

