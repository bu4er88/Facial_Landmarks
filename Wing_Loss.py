def Wing_Loss(w, e):
    """Wing loss"""
    def wing_loss(y_true, y_pred):
        x = tf.reduce_sum(tf.abs(y_true - y_pred))
        if x < w:
            loss = w * tf.math.log(1 + x/e)
        else:
            C = w - w * tf.math.log(1 + w/e)
            loss = x - C
        return loss
    return wing_loss