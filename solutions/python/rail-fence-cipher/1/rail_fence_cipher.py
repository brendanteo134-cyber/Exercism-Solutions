def encode(message, rails):
    fence={}
    for rail in range(rails):
        fence[rail] = ""
    rail = idx = 0
    for x in range(len(message)):
        fence[rail] += message[idx]
        div, _ = divmod(x, rails-1)
        # zig and zag
        if div % 2 == 0:
            rail += 1
        else:
            rail -= 1
        idx += 1
    return "".join(fence[rail] for rail in sorted(fence.keys()))
def decode(message, rails):
    original ="ABCDEFGHIJKLMNOPQRTUVWXYZabcdefghijklmnopqrtuvwxyz1234567890"
    encoded  = encode(original[:len(message)], rails)
    return "".join(message[encoded.index(original[idx])] for idx in range(len(message)))