teacher = models.load_model('THE PATH OF THE PRE-TRAINED TEACHER MODEL/teacher.h5')

student = 
distiller = Distiller(student=student, teacher=teacher)
distiller.compile(
    optimizer=keras.optimizers.Adam(#the learning rate),
    metrics=['accuracy'],
    student_loss_fn=keras.losses.BinaryCrossentropy(),
    distillation_loss_fn=keras.losses.BinaryCrossentropy(),
    alpha=# [0-1],
    )
distiller.fit(x_train, y_train,batch_size=batch_size, epochs=epochs,verbose=0)
