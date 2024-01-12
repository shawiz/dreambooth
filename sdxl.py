import replicate

training = replicate.trainings.create(
    version="stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
    input={
        "input_images": "https://my-domain/my-input-images.zip",
    },
    destination="my-name/my-model"
)
print(training)