---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:4704
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: silk pink saree
  sentences:
  - Cotton Rich Polka Dot Joggers (2-8 Yrs) A playful choice for weekends, these cotton-rich
    joggers pop with a polka dot print. Comfy regular fit with an elasticated drawstring
    waist and neat cuffed legs. Complete with handy pockets on the side.
  - 'Sea Green Embroidered Chinon Silk Kurta Set Main Colour : Sea Green<br/> Package
    Contents : 3<br/> Components : Kurta , Pants, Dupatta<br/> Fabric : Chinon Silk<br/>
    Work : Embroidered<br/>'
  - 'Pink Kanjivaram Silk Saree T801463 '
- source_sentence: festive yellow saree
  sentences:
  - 'Mustard Yellow Crepe Mirrorwork Saree With Matching Blouse Piece Mustard yellow
    saree in crepe with mirrorwork detailing for a traditional look. The design brings
    subtle shine and texture to the drape. Comes with a matching blouse piece and
    Koskii premium quality. A lovely choice for festive celebrations. Disclaimer:
    The blouse worn by the model might be for modelling purpose only. Check the image
    of the blouse piece to understand how the actual blouse piece looks like.'
  - Mashroo navy blue fabric Formal wear pretty navy blue single color blended Mashroo
    soft body designed ajrakh print fabric
  - Khaki Beige Tussar Blouse T739954 This blue tussar blouse has floral embroidered
    all over. Product code is T739954.
- source_sentence: tussar black saree
  sentences:
  - Mauve embroidered kurta set available only at Pernia's Pop Up Shop. Featuring
    a mauve printed sleeveless short kurta in georgette base with sequins, zardosi
    and thread work embroidery. It is paired with a matching lavender gharara pants
    in chanderi silk base and dupatta in net base.
  - 'Wrap Cotton Top in White The wrap top that earns its place in your work or weekend
    wardrobe. Made from a crisp cotton, this smart casual top features a collar neckline
    that sharpens the look instantly, short cap sleeves for a neat, polished finish,
    a tapered silhouette that fits the body with quiet precision, a delicate trim
    detail that adds a refined, considered edge, a dramatic hemline that gives the
    whole look its final, contemporary flourish, and a button closure. Pair it with
    tailored trousers for the office or flared denim for a cool, casual look. Set
    Includes: Top'
  - silk tussar black fabric Formal wear pretty black single color pure silk tussar
    natural plain body fabric
- source_sentence: blue red saree
  sentences:
  - Mauve Printed Formal Half Sleeves Polo Collar Men Regular Fit T-Shirt &#x3C;p&#x3E;Elevate
    your formal wardrobe with this Van Heusen t-shirt. Crafted from a blend of cotton,
    polyester, and spandex, it offers exceptional comfort and a flattering fit. The
    stylish pink color, paired with a chic printed design, ensures you stand out at
    any event. With a sophisticated polo neckline, this t-shirt seamlessly combines
    elegance and ease, making it the perfect choice for those who appreciate refined
    style. Embrace the Move collection for a fresh addition to your ensemble.&#x3C;/p&#x3E;
  - Blue Viscose Blend Straight Embroidered Kurta Palazzo Suit Set *
  - 'Purple Viscose Rayon Paisley Printed Straight Kurta Soft purple kurta featuring
    intricate paisley and floral motifs in a delicate print, elevated by lace detailing
    on the sleeves. Crafted in lightweight viscose rayon, this straight-fit piece
    offers a refined ethnic look with a graceful silhouette.


    Kurta Details:



    All-over paisley and floral print on a soft purple base

    Round neckline with clean detailing

    3/4th sleeves finished with lace accents

    Straight fit with a flowing hem

    Soft viscose rayon fabric



    BIBA Recommends:

    Pair this kurta with solid contrasting bottoms and minimal jewellery to highlight
    the intricate print, ideal for daytime gatherings and soft festive occasions.'
- source_sentence: festive purple saree
  sentences:
  - 'White Hand Embroidered Cotton Dobby Short Kurta For Men <p>Colour : White<br/>
    Package Contents : 1<br/> Fabric : Cotton<br/> Neck : Band Collar<br/> Sleeve
    : Full<br/> Pattern : Hand Embroidered<br/> Closure : Buttons<br/> Fit : Relaxed</p>'
  - Light Olive Solid Slim Fit T-Shirt Cut in a slim fit, this T-shirt delivers a
    streamlined silhouette with a modern touch. The contrast collar adds a subtle
    design detail, while the olive tone keeps the look grounded. Suitable for refined
    casual wear.
  - 'Purple Pure Silk Buti Gold Zariwork Saree With Matching Blouse Piece Purple silk
    saree in pure silk featuring a Dharmavaram weave with a buti weave pattern and
    a medium border, detailed with zariwork in gold for a rich traditional look. Comes
    with a matching blouse piece and Koskii premium quality. A lovely choice for festive
    celebrations. Disclaimer: The blouse worn by the model might be for modelling
    purpose only. Check the image of the blouse piece to understand how the actual
    blouse piece looks like.'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41 -->
- **Maximum Sequence Length:** 128 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'BertModel'})
  (1): Pooling({'embedding_dimension': 384, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'festive purple saree',
    'Purple Pure Silk Buti Gold Zariwork Saree With Matching Blouse Piece Purple silk saree in pure silk featuring a Dharmavaram weave with a buti weave pattern and a medium border, detailed with zariwork in gold for a rich traditional look. Comes with a matching blouse piece and Koskii premium quality. A lovely choice for festive celebrations. Disclaimer: The blouse worn by the model might be for modelling purpose only. Check the image of the blouse piece to understand how the actual blouse piece looks like.',
    'Light Olive Solid Slim Fit T-Shirt Cut in a slim fit, this T-shirt delivers a streamlined silhouette with a modern touch. The contrast collar adds a subtle design detail, while the olive tone keeps the look grounded. Suitable for refined casual wear.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.6663, 0.1710],
#         [0.6663, 1.0000, 0.3209],
#         [0.1710, 0.3209, 1.0000]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 4,704 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                      | sentence_1                                                                        |
  |:---------|:--------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type     | string                                                                          | string                                                                            |
  | modality | text                                                                            | text                                                                              |
  | details  | <ul><li>min: 5 tokens</li><li>mean: 6.09 tokens</li><li>max: 8 tokens</li></ul> | <ul><li>min: 8 tokens</li><li>mean: 71.5 tokens</li><li>max: 128 tokens</li></ul> |
* Samples:
  | sentence_0                      | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  |:--------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>tussar saree</code>       | <code>Beige Tussar Printed Saree T728366 This beige tussar saree has floral prints all over the body. The saree is accompanied with a contrast blouse. Product code is T728366.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | <code>red casual saree</code>   | <code>Red Printed Regular Fit T-Shirt Quiet details strong presence. This t shirt brings a modern edge in red regular fit printed half sleeves round neck. Perfect for casual outings with an easy confident mood. Style it with high rise jeans and white sneakers.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  | <code>cotton green saree</code> | <code>Graceful Essence Designer Silk Cotton Embroidered Readymade Blouse Style Code  <br>: MDU - M15112025114322  <br>  <br>  <br>Material  <br>: Silk Cotton  <br>  <br>  <br>Color  <br>: Deep Sea Green  <br>  <br>  <br>Sleeve  <br>: Half Sleeve  <br>  <br>  <br>Closure  <br>: Front Side   <br>  <br>  <br>Closure Type  <br>: Hook  <br>  <br>  <br>Weight   <br>: 0.300 kg   <br>  <br>  <br>Wash  <br>: Machine Wash  <br>  <br>  <br>Shipping  <br>: Worldwide Available  <br>  <br>  <br>Country of Origin  <br>: India  <br>  <br>  <br>Manufacturer  <br>: SCM Silks Pvt.Ltd., 74,New Market Street, Tirupur, Tamilnadu 641604, India.  <br>  <br>  <br>Reseller &amp; Packer   <br>: Prime Store., 77,New Market Street, Tirupur, Tamilnadu 641604, India.  <br>  <br>  <br>Disclaimer  <br>: PRODUCT COLOR MAY SLIGHTLY VARY DUE TO PHOTOGRAPHIC LIGHTING SOURCES OR YOUR MONITOR SETTINGS</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false,
      "directions": [
          "query_to_doc"
      ],
      "partition_mode": "joint",
      "hardness_mode": null,
      "hardness_strength": 0.0
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `num_train_epochs`: 1
- `fp16`: True
- `per_device_eval_batch_size`: 32
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 32
- `num_train_epochs`: 1
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 32
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Time
- **Training**: 17.8 minutes

### Framework Versions
- Python: 3.13.16
- Sentence Transformers: 5.7.0
- Transformers: 5.18.0
- PyTorch: 2.11.0+cpu
- Accelerate: 1.15.0
- Datasets: 4.8.5
- Tokenizers: 0.23.2

## Additional Resources

- [Training and Finetuning Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-sentence-transformers): the end-to-end guide for training or finetuning Sentence Transformer models.
- [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka): variable-size embeddings that can be truncated with minimal quality loss.
- [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): train multimodal embedding models, with a Visual Document Retrieval walkthrough.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->