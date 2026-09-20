class Solution:
    def productExceptSelf(self, v: List[int]) -> List[int]:
        zero_indices = [i for i, x in enumerate(v) if x == 0]
        n = len(v)
        # --- Case: two or more zeros -> every output is 0 ---
        if len(zero_indices) >= 2:
            return [0] * n
    
        # --- Case: exactly one zero ---
        if len(zero_indices) == 1:
            zero_idx = zero_indices[0]
            product_of_rest = 1
            for j, x in enumerate(v):
                if j != zero_idx:
                    product_of_rest *= x
            w = [0] * n
            w[zero_idx] = product_of_rest
            return w
    
        # --- Case: no zeros -> log-magnitude + sign-parity method ---
        log_mags = [math.log(abs(x)) for x in v]
        signs = [1 if x > 0 else -1 for x in v]
    
        total_log_mag = sum(log_mags)
        total_sign_bits = sum(1 for s in signs if s < 0)  # count of negative entries
    
        w = [0.0] * n
        for i in range(n):
            # Magnitude: sum of all logs except i, exponentiated back
            log_mag_i = total_log_mag - log_mags[i]
            magnitude = math.exp(log_mag_i)
    
            # Sign: parity of negative entries excluding i
            neg_count_excl_i = total_sign_bits - (1 if signs[i] < 0 else 0)
            sign = -1 if (neg_count_excl_i % 2 == 1) else 1
    
            # Round to nearest integer if the input looks integral, to clean up
            # floating point noise from exp(log(...)).
            w[i] = round(sign * magnitude)
    
        return w
    
    