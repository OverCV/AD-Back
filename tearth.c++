/* #### Code section: decls ### */
static PyObject *__pyx_pf_5pyemd_3emd__validate_emd_input(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_first_histogram, PyObject *__pyx_v_second_histogram, PyObject *__pyx_v_distance_matrix);                                                                                                 /* proto */
static PyObject *__pyx_pf_5pyemd_3emd_12__defaults__(CYTHON_UNUSED PyObject *__pyx_self);                                                                                                                                                                                                                /* proto */
static PyObject *__pyx_pf_5pyemd_3emd_2emd(CYTHON_UNUSED PyObject *__pyx_self, PyArrayObject *__pyx_v_first_histogram, PyArrayObject *__pyx_v_second_histogram, PyArrayObject *__pyx_v_distance_matrix, PyObject *__pyx_v_extra_mass_penalty);                                                           /* proto */
static PyObject *__pyx_pf_5pyemd_3emd_14__defaults__(CYTHON_UNUSED PyObject *__pyx_self);                                                                                                                                                                                                                /* proto */
static PyObject *__pyx_pf_5pyemd_3emd_4emd_with_flow(CYTHON_UNUSED PyObject *__pyx_self, PyArrayObject *__pyx_v_first_histogram, PyArrayObject *__pyx_v_second_histogram, PyArrayObject *__pyx_v_distance_matrix, PyObject *__pyx_v_extra_mass_penalty);                                                 /* proto */
static PyObject *__pyx_pf_5pyemd_3emd_6euclidean_pairwise_distance_matrix(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_x);                                                                                                                                                                      /* proto */
static PyObject *__pyx_pf_5pyemd_3emd_8get_bins(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_a, PyObject *__pyx_v_bins, PyObject *__pyx_v_kwargs);                                                                                                                                              /* proto */
static PyObject *__pyx_pf_5pyemd_3emd_16__defaults__(CYTHON_UNUSED PyObject *__pyx_self);                                                                                                                                                                                                                /* proto */
static PyObject *__pyx_pf_5pyemd_3emd_10emd_samples(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_first_array, PyObject *__pyx_v_second_array, PyObject *__pyx_v_extra_mass_penalty, PyObject *__pyx_v_distance, PyObject *__pyx_v_normalized, PyObject *__pyx_v_bins, PyObject *__pyx_v_range); /* proto */
/* #### Code section: late_includes ### */
/* #### Code section: module_state ### */
typedef struct
{
    PyObject *__pyx_d;
    PyObject *__pyx_b;
    PyObject *__pyx_cython_runtime;
    PyObject *__pyx_empty_tuple;
    PyObject *__pyx_empty_bytes;
    PyObject *__pyx_empty_unicode;
#ifdef __Pyx_CyFunction_USED
    PyTypeObject *__pyx_CyFunctionType;
#endif
#ifdef __Pyx_FusedFunction_USED
    PyTypeObject *__pyx_FusedFunctionType;
#endif
#ifdef __Pyx_Generator_USED
    PyTypeObject *__pyx_GeneratorType;
#endif
#ifdef __Pyx_IterableCoroutine_USED
    PyTypeObject *__pyx_IterableCoroutineType;
#endif
#ifdef __Pyx_Coroutine_USED
    PyTypeObject *__pyx_CoroutineAwaitType;
#endif
#ifdef __Pyx_Coroutine_USED
    PyTypeObject *__pyx_CoroutineType;
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
    PyTypeObject *__pyx_ptype_7cpython_4type_type;
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
    PyTypeObject *__pyx_ptype_5numpy_dtype;
    PyTypeObject *__pyx_ptype_5numpy_flatiter;
    PyTypeObject *__pyx_ptype_5numpy_broadcast;
    PyTypeObject *__pyx_ptype_5numpy_ndarray;
    PyTypeObject *__pyx_ptype_5numpy_generic;
    PyTypeObject *__pyx_ptype_5numpy_number;
    PyTypeObject *__pyx_ptype_5numpy_integer;
    PyTypeObject *__pyx_ptype_5numpy_signedinteger;
    PyTypeObject *__pyx_ptype_5numpy_unsignedinteger;
    PyTypeObject *__pyx_ptype_5numpy_inexact;
    PyTypeObject *__pyx_ptype_5numpy_floating;
    PyTypeObject *__pyx_ptype_5numpy_complexfloating;
    PyTypeObject *__pyx_ptype_5numpy_flexible;
    PyTypeObject *__pyx_ptype_5numpy_character;
    PyTypeObject *__pyx_ptype_5numpy_ufunc;
#if CYTHON_USE_MODULE_STATE
#endif
    PyObject *__pyx_kp_u_1_15_0;
    PyObject *__pyx_kp_u_Arrays_of_samples_cannot_be_empt;
    PyObject *__pyx_n_s_DEFAULT_EXTRA_MASS_PENALTY;
    PyObject *__pyx_kp_u_Distance_matrix_must_be_square_c;
    PyObject *__pyx_kp_u_Distance_matrix_must_have_at_lea;
    PyObject *__pyx_kp_u_Histogram_lengths_cannot_be_grea;
    PyObject *__pyx_kp_u_Histogram_lengths_must_be_equal;
    PyObject *__pyx_n_s_ImportError;
    PyObject *__pyx_n_s_MemoryError;
    PyObject *__pyx_n_s_ValueError;
    PyObject *__pyx_kp_u__10;
    PyObject *__pyx_n_s__11;
    PyObject *__pyx_n_s__23;
    PyObject *__pyx_n_s__26;
    PyObject *__pyx_n_s_a;
    PyObject *__pyx_n_s_abs;
    PyObject *__pyx_n_s_array;
    PyObject *__pyx_n_s_astype;
    PyObject *__pyx_n_s_asyncio_coroutines;
    PyObject *__pyx_n_u_auto;
    PyObject *__pyx_n_s_axis;
    PyObject *__pyx_n_s_bin_edges;
    PyObject *__pyx_n_s_bin_locations;
    PyObject *__pyx_n_s_bins;
    PyObject *__pyx_n_s_cline_in_traceback;
    PyObject *__pyx_n_s_concatenate;
    PyObject *__pyx_n_s_distance;
    PyObject *__pyx_n_s_distance_matrix;
    PyObject *__pyx_n_s_emd;
    PyObject *__pyx_n_s_emd_samples;
    PyObject *__pyx_n_s_emd_with_flow;
    PyObject *__pyx_n_u_euclidean;
    PyObject *__pyx_n_s_euclidean_pairwise_distance_matr;
    PyObject *__pyx_n_s_extra_mass_penalty;
    PyObject *__pyx_n_s_first_array;
    PyObject *__pyx_n_s_first_histogram;
    PyObject *__pyx_n_s_float64;
    PyObject *__pyx_n_s_get_bins;
    PyObject *__pyx_n_s_hist;
    PyObject *__pyx_n_s_histogram;
    PyObject *__pyx_n_s_histogram_bin_edges;
    PyObject *__pyx_n_s_import;
    PyObject *__pyx_n_s_initializing;
    PyObject *__pyx_n_s_is_coroutine;
    PyObject *__pyx_n_s_items;
    PyObject *__pyx_n_s_kwargs;
    PyObject *__pyx_n_s_main;
    PyObject *__pyx_n_s_max;
    PyObject *__pyx_n_s_mean;
    PyObject *__pyx_n_s_min;
    PyObject *__pyx_n_s_name;
    PyObject *__pyx_n_s_normalized;
    PyObject *__pyx_n_s_np;
    PyObject *__pyx_n_s_numpy;
    PyObject *__pyx_kp_u_numpy_core_multiarray_failed_to;
    PyObject *__pyx_kp_u_numpy_core_umath_failed_to_impor;
    PyObject *__pyx_n_s_parse_version;
    PyObject *__pyx_n_s_pkg_resources;
    PyObject *__pyx_n_s_pyemd_emd;
    PyObject *__pyx_n_s_range;
    PyObject *__pyx_n_s_repeat;
    PyObject *__pyx_n_s_reshape;
    PyObject *__pyx_n_s_second_array;
    PyObject *__pyx_n_s_second_histogram;
    PyObject *__pyx_n_s_shape;
    PyObject *__pyx_n_s_size;
    PyObject *__pyx_n_s_spec;
    PyObject *__pyx_kp_s_src_pyemd_emd_pyx;
    PyObject *__pyx_n_s_sum;
    PyObject *__pyx_n_s_test;
    PyObject *__pyx_n_s_tile;
    PyObject *__pyx_n_s_validate_emd_input;
    PyObject *__pyx_n_s_version;
    PyObject *__pyx_n_s_x;
    PyObject *__pyx_float_neg_1_0;
    PyObject *__pyx_int_0;
    PyObject *__pyx_int_1;
    PyObject *__pyx_int_10;
    PyObject *__pyx_int_neg_1;
    PyObject *__pyx_tuple_;
    PyObject *__pyx_slice__6;
    PyObject *__pyx_slice__7;
    PyObject *__pyx_tuple__2;
    PyObject *__pyx_tuple__3;
    PyObject *__pyx_tuple__4;
    PyObject *__pyx_tuple__5;
    PyObject *__pyx_tuple__8;
    PyObject *__pyx_tuple__9;
    PyObject *__pyx_tuple__12;
    PyObject *__pyx_tuple__14;
    PyObject *__pyx_tuple__17;
    PyObject *__pyx_tuple__19;
    PyObject *__pyx_tuple__20;
    PyObject *__pyx_tuple__22;
    PyObject *__pyx_tuple__24;
    PyObject *__pyx_codeobj__13;
    PyObject *__pyx_codeobj__15;
    PyObject *__pyx_codeobj__16;
    PyObject *__pyx_codeobj__18;
    PyObject *__pyx_codeobj__21;
    PyObject *__pyx_codeobj__25;
} __pyx_mstate;

#if CYTHON_USE_MODULE_STATE
#ifdef __cplusplus
namespace
{
    extern struct PyModuleDef __pyx_moduledef;
} /* anonymous namespace */
#else
static struct PyModuleDef __pyx_moduledef;
#endif

#define __pyx_mstate(o) ((__pyx_mstate *)__Pyx_PyModule_GetState(o))

#define __pyx_mstate_global (__pyx_mstate(PyState_FindModule(&__pyx_moduledef)))

#define __pyx_m (PyState_FindModule(&__pyx_moduledef))
#else
static __pyx_mstate __pyx_mstate_global_static =
#ifdef __cplusplus
    {};
#else
    {0};
#endif
static __pyx_mstate *__pyx_mstate_global = &__pyx_mstate_global_static;
#endif
/* #### Code section: module_state_clear ### */
#if CYTHON_USE_MODULE_STATE
static int __pyx_m_clear(PyObject *m)
{
    __pyx_mstate *clear_module_state = __pyx_mstate(m);
    if (!clear_module_state)
        return 0;
    Py_CLEAR(clear_module_state->__pyx_d);
    Py_CLEAR(clear_module_state->__pyx_b);
    Py_CLEAR(clear_module_state->__pyx_cython_runtime);
    Py_CLEAR(clear_module_state->__pyx_empty_tuple);
    Py_CLEAR(clear_module_state->__pyx_empty_bytes);
    Py_CLEAR(clear_module_state->__pyx_empty_unicode);
#ifdef __Pyx_CyFunction_USED
    Py_CLEAR(clear_module_state->__pyx_CyFunctionType);
#endif
#ifdef __Pyx_FusedFunction_USED
    Py_CLEAR(clear_module_state->__pyx_FusedFunctionType);
#endif
    Py_CLEAR(clear_module_state->__pyx_ptype_7cpython_4type_type);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_dtype);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_flatiter);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_broadcast);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_ndarray);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_generic);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_number);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_integer);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_signedinteger);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_unsignedinteger);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_inexact);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_floating);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_complexfloating);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_flexible);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_character);
    Py_CLEAR(clear_module_state->__pyx_ptype_5numpy_ufunc);
    Py_CLEAR(clear_module_state->__pyx_kp_u_1_15_0);
    Py_CLEAR(clear_module_state->__pyx_kp_u_Arrays_of_samples_cannot_be_empt);
    Py_CLEAR(clear_module_state->__pyx_n_s_DEFAULT_EXTRA_MASS_PENALTY);
    Py_CLEAR(clear_module_state->__pyx_kp_u_Distance_matrix_must_be_square_c);
    Py_CLEAR(clear_module_state->__pyx_kp_u_Distance_matrix_must_have_at_lea);
    Py_CLEAR(clear_module_state->__pyx_kp_u_Histogram_lengths_cannot_be_grea);
    Py_CLEAR(clear_module_state->__pyx_kp_u_Histogram_lengths_must_be_equal);
    Py_CLEAR(clear_module_state->__pyx_n_s_ImportError);
    Py_CLEAR(clear_module_state->__pyx_n_s_MemoryError);
    Py_CLEAR(clear_module_state->__pyx_n_s_ValueError);
    Py_CLEAR(clear_module_state->__pyx_kp_u__10);
    Py_CLEAR(clear_module_state->__pyx_n_s__11);
    Py_CLEAR(clear_module_state->__pyx_n_s__23);
    Py_CLEAR(clear_module_state->__pyx_n_s__26);
    Py_CLEAR(clear_module_state->__pyx_n_s_a);
    Py_CLEAR(clear_module_state->__pyx_n_s_abs);
    Py_CLEAR(clear_module_state->__pyx_n_s_array);
    Py_CLEAR(clear_module_state->__pyx_n_s_astype);
    Py_CLEAR(clear_module_state->__pyx_n_s_asyncio_coroutines);
    Py_CLEAR(clear_module_state->__pyx_n_u_auto);
    Py_CLEAR(clear_module_state->__pyx_n_s_axis);
    Py_CLEAR(clear_module_state->__pyx_n_s_bin_edges);
    Py_CLEAR(clear_module_state->__pyx_n_s_bin_locations);
    Py_CLEAR(clear_module_state->__pyx_n_s_bins);
    Py_CLEAR(clear_module_state->__pyx_n_s_cline_in_traceback);
    Py_CLEAR(clear_module_state->__pyx_n_s_concatenate);
    Py_CLEAR(clear_module_state->__pyx_n_s_distance);
    Py_CLEAR(clear_module_state->__pyx_n_s_distance_matrix);
    Py_CLEAR(clear_module_state->__pyx_n_s_emd);
    Py_CLEAR(clear_module_state->__pyx_n_s_emd_samples);
    Py_CLEAR(clear_module_state->__pyx_n_s_emd_with_flow);
    Py_CLEAR(clear_module_state->__pyx_n_u_euclidean);
    Py_CLEAR(clear_module_state->__pyx_n_s_euclidean_pairwise_distance_matr);
    Py_CLEAR(clear_module_state->__pyx_n_s_extra_mass_penalty);
    Py_CLEAR(clear_module_state->__pyx_n_s_first_array);
    Py_CLEAR(clear_module_state->__pyx_n_s_first_histogram);
    Py_CLEAR(clear_module_state->__pyx_n_s_float64);
    Py_CLEAR(clear_module_state->__pyx_n_s_get_bins);
    Py_CLEAR(clear_module_state->__pyx_n_s_hist);
    Py_CLEAR(clear_module_state->__pyx_n_s_histogram);
    Py_CLEAR(clear_module_state->__pyx_n_s_histogram_bin_edges);
    Py_CLEAR(clear_module_state->__pyx_n_s_import);
    Py_CLEAR(clear_module_state->__pyx_n_s_initializing);
    Py_CLEAR(clear_module_state->__pyx_n_s_is_coroutine);
    Py_CLEAR(clear_module_state->__pyx_n_s_items);
    Py_CLEAR(clear_module_state->__pyx_n_s_kwargs);
    Py_CLEAR(clear_module_state->__pyx_n_s_main);
    Py_CLEAR(clear_module_state->__pyx_n_s_max);
    Py_CLEAR(clear_module_state->__pyx_n_s_mean);
    Py_CLEAR(clear_module_state->__pyx_n_s_min);
    Py_CLEAR(clear_module_state->__pyx_n_s_name);
    Py_CLEAR(clear_module_state->__pyx_n_s_normalized);
    Py_CLEAR(clear_module_state->__pyx_n_s_np);
    Py_CLEAR(clear_module_state->__pyx_n_s_numpy);
    Py_CLEAR(clear_module_state->__pyx_kp_u_numpy_core_multiarray_failed_to);
    Py_CLEAR(clear_module_state->__pyx_kp_u_numpy_core_umath_failed_to_impor);
    Py_CLEAR(clear_module_state->__pyx_n_s_parse_version);
    Py_CLEAR(clear_module_state->__pyx_n_s_pkg_resources);
    Py_CLEAR(clear_module_state->__pyx_n_s_pyemd_emd);
    Py_CLEAR(clear_module_state->__pyx_n_s_range);
    Py_CLEAR(clear_module_state->__pyx_n_s_repeat);
    Py_CLEAR(clear_module_state->__pyx_n_s_reshape);
    Py_CLEAR(clear_module_state->__pyx_n_s_second_array);
    Py_CLEAR(clear_module_state->__pyx_n_s_second_histogram);
    Py_CLEAR(clear_module_state->__pyx_n_s_shape);
    Py_CLEAR(clear_module_state->__pyx_n_s_size);
    Py_CLEAR(clear_module_state->__pyx_n_s_spec);
    Py_CLEAR(clear_module_state->__pyx_kp_s_src_pyemd_emd_pyx);
    Py_CLEAR(clear_module_state->__pyx_n_s_sum);
    Py_CLEAR(clear_module_state->__pyx_n_s_test);
    Py_CLEAR(clear_module_state->__pyx_n_s_tile);
    Py_CLEAR(clear_module_state->__pyx_n_s_validate_emd_input);
    Py_CLEAR(clear_module_state->__pyx_n_s_version);
    Py_CLEAR(clear_module_state->__pyx_n_s_x);
    Py_CLEAR(clear_module_state->__pyx_float_neg_1_0);
    Py_CLEAR(clear_module_state->__pyx_int_0);
    Py_CLEAR(clear_module_state->__pyx_int_1);
    Py_CLEAR(clear_module_state->__pyx_int_10);
    Py_CLEAR(clear_module_state->__pyx_int_neg_1);
    Py_CLEAR(clear_module_state->__pyx_tuple_);
    Py_CLEAR(clear_module_state->__pyx_slice__6);
    Py_CLEAR(clear_module_state->__pyx_slice__7);
    Py_CLEAR(clear_module_state->__pyx_tuple__2);
    Py_CLEAR(clear_module_state->__pyx_tuple__3);
    Py_CLEAR(clear_module_state->__pyx_tuple__4);
    Py_CLEAR(clear_module_state->__pyx_tuple__5);
    Py_CLEAR(clear_module_state->__pyx_tuple__8);
    Py_CLEAR(clear_module_state->__pyx_tuple__9);
    Py_CLEAR(clear_module_state->__pyx_tuple__12);
    Py_CLEAR(clear_module_state->__pyx_tuple__14);
    Py_CLEAR(clear_module_state->__pyx_tuple__17);
    Py_CLEAR(clear_module_state->__pyx_tuple__19);
    Py_CLEAR(clear_module_state->__pyx_tuple__20);
    Py_CLEAR(clear_module_state->__pyx_tuple__22);
    Py_CLEAR(clear_module_state->__pyx_tuple__24);
    Py_CLEAR(clear_module_state->__pyx_codeobj__13);
    Py_CLEAR(clear_module_state->__pyx_codeobj__15);
    Py_CLEAR(clear_module_state->__pyx_codeobj__16);
    Py_CLEAR(clear_module_state->__pyx_codeobj__18);
    Py_CLEAR(clear_module_state->__pyx_codeobj__21);
    Py_CLEAR(clear_module_state->__pyx_codeobj__25);
    return 0;
}
#endif
/* #### Code section: module_state_traverse ### */
#if CYTHON_USE_MODULE_STATE
static int __pyx_m_traverse(PyObject *m, visitproc visit, void *arg)
{
    __pyx_mstate *traverse_module_state = __pyx_mstate(m);
    if (!traverse_module_state)
        return 0;
    Py_VISIT(traverse_module_state->__pyx_d);
    Py_VISIT(traverse_module_state->__pyx_b);
    Py_VISIT(traverse_module_state->__pyx_cython_runtime);
    Py_VISIT(traverse_module_state->__pyx_empty_tuple);
    Py_VISIT(traverse_module_state->__pyx_empty_bytes);
    Py_VISIT(traverse_module_state->__pyx_empty_unicode);
#ifdef __Pyx_CyFunction_USED
    Py_VISIT(traverse_module_state->__pyx_CyFunctionType);
#endif
#ifdef __Pyx_FusedFunction_USED
    Py_VISIT(traverse_module_state->__pyx_FusedFunctionType);
#endif
    Py_VISIT(traverse_module_state->__pyx_ptype_7cpython_4type_type);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_dtype);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_flatiter);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_broadcast);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_ndarray);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_generic);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_number);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_integer);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_signedinteger);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_unsignedinteger);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_inexact);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_floating);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_complexfloating);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_flexible);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_character);
    Py_VISIT(traverse_module_state->__pyx_ptype_5numpy_ufunc);
    Py_VISIT(traverse_module_state->__pyx_kp_u_1_15_0);
    Py_VISIT(traverse_module_state->__pyx_kp_u_Arrays_of_samples_cannot_be_empt);
    Py_VISIT(traverse_module_state->__pyx_n_s_DEFAULT_EXTRA_MASS_PENALTY);
    Py_VISIT(traverse_module_state->__pyx_kp_u_Distance_matrix_must_be_square_c);
    Py_VISIT(traverse_module_state->__pyx_kp_u_Distance_matrix_must_have_at_lea);
    Py_VISIT(traverse_module_state->__pyx_kp_u_Histogram_lengths_cannot_be_grea);
    Py_VISIT(traverse_module_state->__pyx_kp_u_Histogram_lengths_must_be_equal);
    Py_VISIT(traverse_module_state->__pyx_n_s_ImportError);
    Py_VISIT(traverse_module_state->__pyx_n_s_MemoryError);
    Py_VISIT(traverse_module_state->__pyx_n_s_ValueError);
    Py_VISIT(traverse_module_state->__pyx_kp_u__10);
    Py_VISIT(traverse_module_state->__pyx_n_s__11);
    Py_VISIT(traverse_module_state->__pyx_n_s__23);
    Py_VISIT(traverse_module_state->__pyx_n_s__26);
    Py_VISIT(traverse_module_state->__pyx_n_s_a);
    Py_VISIT(traverse_module_state->__pyx_n_s_abs);
    Py_VISIT(traverse_module_state->__pyx_n_s_array);
    Py_VISIT(traverse_module_state->__pyx_n_s_astype);
    Py_VISIT(traverse_module_state->__pyx_n_s_asyncio_coroutines);
    Py_VISIT(traverse_module_state->__pyx_n_u_auto);
    Py_VISIT(traverse_module_state->__pyx_n_s_axis);
    Py_VISIT(traverse_module_state->__pyx_n_s_bin_edges);
    Py_VISIT(traverse_module_state->__pyx_n_s_bin_locations);
    Py_VISIT(traverse_module_state->__pyx_n_s_bins);
    Py_VISIT(traverse_module_state->__pyx_n_s_cline_in_traceback);
    Py_VISIT(traverse_module_state->__pyx_n_s_concatenate);
    Py_VISIT(traverse_module_state->__pyx_n_s_distance);
    Py_VISIT(traverse_module_state->__pyx_n_s_distance_matrix);
    Py_VISIT(traverse_module_state->__pyx_n_s_emd);
    Py_VISIT(traverse_module_state->__pyx_n_s_emd_samples);
    Py_VISIT(traverse_module_state->__pyx_n_s_emd_with_flow);
    Py_VISIT(traverse_module_state->__pyx_n_u_euclidean);
    Py_VISIT(traverse_module_state->__pyx_n_s_euclidean_pairwise_distance_matr);
    Py_VISIT(traverse_module_state->__pyx_n_s_extra_mass_penalty);
    Py_VISIT(traverse_module_state->__pyx_n_s_first_array);
    Py_VISIT(traverse_module_state->__pyx_n_s_first_histogram);
    Py_VISIT(traverse_module_state->__pyx_n_s_float64);
    Py_VISIT(traverse_module_state->__pyx_n_s_get_bins);
    Py_VISIT(traverse_module_state->__pyx_n_s_hist);
    Py_VISIT(traverse_module_state->__pyx_n_s_histogram);
    Py_VISIT(traverse_module_state->__pyx_n_s_histogram_bin_edges);
    Py_VISIT(traverse_module_state->__pyx_n_s_import);
    Py_VISIT(traverse_module_state->__pyx_n_s_initializing);
    Py_VISIT(traverse_module_state->__pyx_n_s_is_coroutine);
    Py_VISIT(traverse_module_state->__pyx_n_s_items);
    Py_VISIT(traverse_module_state->__pyx_n_s_kwargs);
    Py_VISIT(traverse_module_state->__pyx_n_s_main);
    Py_VISIT(traverse_module_state->__pyx_n_s_max);
    Py_VISIT(traverse_module_state->__pyx_n_s_mean);
    Py_VISIT(traverse_module_state->__pyx_n_s_min);
    Py_VISIT(traverse_module_state->__pyx_n_s_name);
    Py_VISIT(traverse_module_state->__pyx_n_s_normalized);
    Py_VISIT(traverse_module_state->__pyx_n_s_np);
    Py_VISIT(traverse_module_state->__pyx_n_s_numpy);
    Py_VISIT(traverse_module_state->__pyx_kp_u_numpy_core_multiarray_failed_to);
    Py_VISIT(traverse_module_state->__pyx_kp_u_numpy_core_umath_failed_to_impor);
    Py_VISIT(traverse_module_state->__pyx_n_s_parse_version);
    Py_VISIT(traverse_module_state->__pyx_n_s_pkg_resources);
    Py_VISIT(traverse_module_state->__pyx_n_s_pyemd_emd);
    Py_VISIT(traverse_module_state->__pyx_n_s_range);
    Py_VISIT(traverse_module_state->__pyx_n_s_repeat);
    Py_VISIT(traverse_module_state->__pyx_n_s_reshape);
    Py_VISIT(traverse_module_state->__pyx_n_s_second_array);
    Py_VISIT(traverse_module_state->__pyx_n_s_second_histogram);
    Py_VISIT(traverse_module_state->__pyx_n_s_shape);
    Py_VISIT(traverse_module_state->__pyx_n_s_size);
    Py_VISIT(traverse_module_state->__pyx_n_s_spec);
    Py_VISIT(traverse_module_state->__pyx_kp_s_src_pyemd_emd_pyx);
    Py_VISIT(traverse_module_state->__pyx_n_s_sum);
    Py_VISIT(traverse_module_state->__pyx_n_s_test);
    Py_VISIT(traverse_module_state->__pyx_n_s_tile);
    Py_VISIT(traverse_module_state->__pyx_n_s_validate_emd_input);
    Py_VISIT(traverse_module_state->__pyx_n_s_version);
    Py_VISIT(traverse_module_state->__pyx_n_s_x);
    Py_VISIT(traverse_module_state->__pyx_float_neg_1_0);
    Py_VISIT(traverse_module_state->__pyx_int_0);
    Py_VISIT(traverse_module_state->__pyx_int_1);
    Py_VISIT(traverse_module_state->__pyx_int_10);
    Py_VISIT(traverse_module_state->__pyx_int_neg_1);
    Py_VISIT(traverse_module_state->__pyx_tuple_);
    Py_VISIT(traverse_module_state->__pyx_slice__6);
    Py_VISIT(traverse_module_state->__pyx_slice__7);
    Py_VISIT(traverse_module_state->__pyx_tuple__2);
    Py_VISIT(traverse_module_state->__pyx_tuple__3);
    Py_VISIT(traverse_module_state->__pyx_tuple__4);
    Py_VISIT(traverse_module_state->__pyx_tuple__5);
    Py_VISIT(traverse_module_state->__pyx_tuple__8);
    Py_VISIT(traverse_module_state->__pyx_tuple__9);
    Py_VISIT(traverse_module_state->__pyx_tuple__12);
    Py_VISIT(traverse_module_state->__pyx_tuple__14);
    Py_VISIT(traverse_module_state->__pyx_tuple__17);
    Py_VISIT(traverse_module_state->__pyx_tuple__19);
    Py_VISIT(traverse_module_state->__pyx_tuple__20);
    Py_VISIT(traverse_module_state->__pyx_tuple__22);
    Py_VISIT(traverse_module_state->__pyx_tuple__24);
    Py_VISIT(traverse_module_state->__pyx_codeobj__13);
    Py_VISIT(traverse_module_state->__pyx_codeobj__15);
    Py_VISIT(traverse_module_state->__pyx_codeobj__16);
    Py_VISIT(traverse_module_state->__pyx_codeobj__18);
    Py_VISIT(traverse_module_state->__pyx_codeobj__21);
    Py_VISIT(traverse_module_state->__pyx_codeobj__25);
    return 0;
}
#endif
/* #### Code section: module_state_defines ### */
#define __pyx_d __pyx_mstate_global->__pyx_d
#define __pyx_b __pyx_mstate_global->__pyx_b
#define __pyx_cython_runtime __pyx_mstate_global->__pyx_cython_runtime
#define __pyx_empty_tuple __pyx_mstate_global->__pyx_empty_tuple
#define __pyx_empty_bytes __pyx_mstate_global->__pyx_empty_bytes
#define __pyx_empty_unicode __pyx_mstate_global->__pyx_empty_unicode
#ifdef __Pyx_CyFunction_USED
#define __pyx_CyFunctionType __pyx_mstate_global->__pyx_CyFunctionType
#endif
#ifdef __Pyx_FusedFunction_USED
#define __pyx_FusedFunctionType __pyx_mstate_global->__pyx_FusedFunctionType
#endif
#ifdef __Pyx_Generator_USED
#define __pyx_GeneratorType __pyx_mstate_global->__pyx_GeneratorType
#endif
#ifdef __Pyx_IterableCoroutine_USED
#define __pyx_IterableCoroutineType __pyx_mstate_global->__pyx_IterableCoroutineType
#endif
#ifdef __Pyx_Coroutine_USED
#define __pyx_CoroutineAwaitType __pyx_mstate_global->__pyx_CoroutineAwaitType
#endif
#ifdef __Pyx_Coroutine_USED
#define __pyx_CoroutineType __pyx_mstate_global->__pyx_CoroutineType
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#define __pyx_ptype_7cpython_4type_type __pyx_mstate_global->__pyx_ptype_7cpython_4type_type
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#if CYTHON_USE_MODULE_STATE
#endif
#define __pyx_ptype_5numpy_dtype __pyx_mstate_global->__pyx_ptype_5numpy_dtype
#define __pyx_ptype_5numpy_flatiter __pyx_mstate_global->__pyx_ptype_5numpy_flatiter
#define __pyx_ptype_5numpy_broadcast __pyx_mstate_global->__pyx_ptype_5numpy_broadcast
#define __pyx_ptype_5numpy_ndarray __pyx_mstate_global->__pyx_ptype_5numpy_ndarray
#define __pyx_ptype_5numpy_generic __pyx_mstate_global->__pyx_ptype_5numpy_generic
#define __pyx_ptype_5numpy_number __pyx_mstate_global->__pyx_ptype_5numpy_number
#define __pyx_ptype_5numpy_integer __pyx_mstate_global->__pyx_ptype_5numpy_integer
#define __pyx_ptype_5numpy_signedinteger __pyx_mstate_global->__pyx_ptype_5numpy_signedinteger
#define __pyx_ptype_5numpy_unsignedinteger __pyx_mstate_global->__pyx_ptype_5numpy_unsignedinteger
#define __pyx_ptype_5numpy_inexact __pyx_mstate_global->__pyx_ptype_5numpy_inexact
#define __pyx_ptype_5numpy_floating __pyx_mstate_global->__pyx_ptype_5numpy_floating
#define __pyx_ptype_5numpy_complexfloating __pyx_mstate_global->__pyx_ptype_5numpy_complexfloating
#define __pyx_ptype_5numpy_flexible __pyx_mstate_global->__pyx_ptype_5numpy_flexible
#define __pyx_ptype_5numpy_character __pyx_mstate_global->__pyx_ptype_5numpy_character
#define __pyx_ptype_5numpy_ufunc __pyx_mstate_global->__pyx_ptype_5numpy_ufunc
#if CYTHON_USE_MODULE_STATE
#endif
#define __pyx_kp_u_1_15_0 __pyx_mstate_global->__pyx_kp_u_1_15_0
#define __pyx_kp_u_Arrays_of_samples_cannot_be_empt __pyx_mstate_global->__pyx_kp_u_Arrays_of_samples_cannot_be_empt
#define __pyx_n_s_DEFAULT_EXTRA_MASS_PENALTY __pyx_mstate_global->__pyx_n_s_DEFAULT_EXTRA_MASS_PENALTY
#define __pyx_kp_u_Distance_matrix_must_be_square_c __pyx_mstate_global->__pyx_kp_u_Distance_matrix_must_be_square_c
#define __pyx_kp_u_Distance_matrix_must_have_at_lea __pyx_mstate_global->__pyx_kp_u_Distance_matrix_must_have_at_lea
#define __pyx_kp_u_Histogram_lengths_cannot_be_grea __pyx_mstate_global->__pyx_kp_u_Histogram_lengths_cannot_be_grea
#define __pyx_kp_u_Histogram_lengths_must_be_equal __pyx_mstate_global->__pyx_kp_u_Histogram_lengths_must_be_equal
#define __pyx_n_s_ImportError __pyx_mstate_global->__pyx_n_s_ImportError
#define __pyx_n_s_MemoryError __pyx_mstate_global->__pyx_n_s_MemoryError
#define __pyx_n_s_ValueError __pyx_mstate_global->__pyx_n_s_ValueError
#define __pyx_kp_u__10 __pyx_mstate_global->__pyx_kp_u__10
#define __pyx_n_s__11 __pyx_mstate_global->__pyx_n_s__11
#define __pyx_n_s__23 __pyx_mstate_global->__pyx_n_s__23
#define __pyx_n_s__26 __pyx_mstate_global->__pyx_n_s__26
#define __pyx_n_s_a __pyx_mstate_global->__pyx_n_s_a
#define __pyx_n_s_abs __pyx_mstate_global->__pyx_n_s_abs
#define __pyx_n_s_array __pyx_mstate_global->__pyx_n_s_array
#define __pyx_n_s_astype __pyx_mstate_global->__pyx_n_s_astype
#define __pyx_n_s_asyncio_coroutines __pyx_mstate_global->__pyx_n_s_asyncio_coroutines
#define __pyx_n_u_auto __pyx_mstate_global->__pyx_n_u_auto
#define __pyx_n_s_axis __pyx_mstate_global->__pyx_n_s_axis
#define __pyx_n_s_bin_edges __pyx_mstate_global->__pyx_n_s_bin_edges
#define __pyx_n_s_bin_locations __pyx_mstate_global->__pyx_n_s_bin_locations
#define __pyx_n_s_bins __pyx_mstate_global->__pyx_n_s_bins
#define __pyx_n_s_cline_in_traceback __pyx_mstate_global->__pyx_n_s_cline_in_traceback
#define __pyx_n_s_concatenate __pyx_mstate_global->__pyx_n_s_concatenate
#define __pyx_n_s_distance __pyx_mstate_global->__pyx_n_s_distance
#define __pyx_n_s_distance_matrix __pyx_mstate_global->__pyx_n_s_distance_matrix
#define __pyx_n_s_emd __pyx_mstate_global->__pyx_n_s_emd
#define __pyx_n_s_emd_samples __pyx_mstate_global->__pyx_n_s_emd_samples
#define __pyx_n_s_emd_with_flow __pyx_mstate_global->__pyx_n_s_emd_with_flow
#define __pyx_n_u_euclidean __pyx_mstate_global->__pyx_n_u_euclidean
#define __pyx_n_s_euclidean_pairwise_distance_matr __pyx_mstate_global->__pyx_n_s_euclidean_pairwise_distance_matr
#define __pyx_n_s_extra_mass_penalty __pyx_mstate_global->__pyx_n_s_extra_mass_penalty
#define __pyx_n_s_first_array __pyx_mstate_global->__pyx_n_s_first_array
#define __pyx_n_s_first_histogram __pyx_mstate_global->__pyx_n_s_first_histogram
#define __pyx_n_s_float64 __pyx_mstate_global->__pyx_n_s_float64
#define __pyx_n_s_get_bins __pyx_mstate_global->__pyx_n_s_get_bins
#define __pyx_n_s_hist __pyx_mstate_global->__pyx_n_s_hist
#define __pyx_n_s_histogram __pyx_mstate_global->__pyx_n_s_histogram
#define __pyx_n_s_histogram_bin_edges __pyx_mstate_global->__pyx_n_s_histogram_bin_edges
#define __pyx_n_s_import __pyx_mstate_global->__pyx_n_s_import
#define __pyx_n_s_initializing __pyx_mstate_global->__pyx_n_s_initializing
#define __pyx_n_s_is_coroutine __pyx_mstate_global->__pyx_n_s_is_coroutine
#define __pyx_n_s_items __pyx_mstate_global->__pyx_n_s_items
#define __pyx_n_s_kwargs __pyx_mstate_global->__pyx_n_s_kwargs
#define __pyx_n_s_main __pyx_mstate_global->__pyx_n_s_main
#define __pyx_n_s_max __pyx_mstate_global->__pyx_n_s_max
#define __pyx_n_s_mean __pyx_mstate_global->__pyx_n_s_mean
#define __pyx_n_s_min __pyx_mstate_global->__pyx_n_s_min
#define __pyx_n_s_name __pyx_mstate_global->__pyx_n_s_name
#define __pyx_n_s_normalized __pyx_mstate_global->__pyx_n_s_normalized
#define __pyx_n_s_np __pyx_mstate_global->__pyx_n_s_np
#define __pyx_n_s_numpy __pyx_mstate_global->__pyx_n_s_numpy
#define __pyx_kp_u_numpy_core_multiarray_failed_to __pyx_mstate_global->__pyx_kp_u_numpy_core_multiarray_failed_to
#define __pyx_kp_u_numpy_core_umath_failed_to_impor __pyx_mstate_global->__pyx_kp_u_numpy_core_umath_failed_to_impor
#define __pyx_n_s_parse_version __pyx_mstate_global->__pyx_n_s_parse_version
#define __pyx_n_s_pkg_resources __pyx_mstate_global->__pyx_n_s_pkg_resources
#define __pyx_n_s_pyemd_emd __pyx_mstate_global->__pyx_n_s_pyemd_emd
#define __pyx_n_s_range __pyx_mstate_global->__pyx_n_s_range
#define __pyx_n_s_repeat __pyx_mstate_global->__pyx_n_s_repeat
#define __pyx_n_s_reshape __pyx_mstate_global->__pyx_n_s_reshape
#define __pyx_n_s_second_array __pyx_mstate_global->__pyx_n_s_second_array
#define __pyx_n_s_second_histogram __pyx_mstate_global->__pyx_n_s_second_histogram
#define __pyx_n_s_shape __pyx_mstate_global->__pyx_n_s_shape
#define __pyx_n_s_size __pyx_mstate_global->__pyx_n_s_size
#define __pyx_n_s_spec __pyx_mstate_global->__pyx_n_s_spec
#define __pyx_kp_s_src_pyemd_emd_pyx __pyx_mstate_global->__pyx_kp_s_src_pyemd_emd_pyx
#define __pyx_n_s_sum __pyx_mstate_global->__pyx_n_s_sum
#define __pyx_n_s_test __pyx_mstate_global->__pyx_n_s_test
#define __pyx_n_s_tile __pyx_mstate_global->__pyx_n_s_tile
#define __pyx_n_s_validate_emd_input __pyx_mstate_global->__pyx_n_s_validate_emd_input
#define __pyx_n_s_version __pyx_mstate_global->__pyx_n_s_version
#define __pyx_n_s_x __pyx_mstate_global->__pyx_n_s_x
#define __pyx_float_neg_1_0 __pyx_mstate_global->__pyx_float_neg_1_0
#define __pyx_int_0 __pyx_mstate_global->__pyx_int_0
#define __pyx_int_1 __pyx_mstate_global->__pyx_int_1
#define __pyx_int_10 __pyx_mstate_global->__pyx_int_10
#define __pyx_int_neg_1 __pyx_mstate_global->__pyx_int_neg_1
#define __pyx_tuple_ __pyx_mstate_global->__pyx_tuple_
#define __pyx_slice__6 __pyx_mstate_global->__pyx_slice__6
#define __pyx_slice__7 __pyx_mstate_global->__pyx_slice__7
#define __pyx_tuple__2 __pyx_mstate_global->__pyx_tuple__2
#define __pyx_tuple__3 __pyx_mstate_global->__pyx_tuple__3
#define __pyx_tuple__4 __pyx_mstate_global->__pyx_tuple__4
#define __pyx_tuple__5 __pyx_mstate_global->__pyx_tuple__5
#define __pyx_tuple__8 __pyx_mstate_global->__pyx_tuple__8
#define __pyx_tuple__9 __pyx_mstate_global->__pyx_tuple__9
#define __pyx_tuple__12 __pyx_mstate_global->__pyx_tuple__12
#define __pyx_tuple__14 __pyx_mstate_global->__pyx_tuple__14
#define __pyx_tuple__17 __pyx_mstate_global->__pyx_tuple__17
#define __pyx_tuple__19 __pyx_mstate_global->__pyx_tuple__19
#define __pyx_tuple__20 __pyx_mstate_global->__pyx_tuple__20
#define __pyx_tuple__22 __pyx_mstate_global->__pyx_tuple__22
#define __pyx_tuple__24 __pyx_mstate_global->__pyx_tuple__24
#define __pyx_codeobj__13 __pyx_mstate_global->__pyx_codeobj__13
#define __pyx_codeobj__15 __pyx_mstate_global->__pyx_codeobj__15
#define __pyx_codeobj__16 __pyx_mstate_global->__pyx_codeobj__16
#define __pyx_codeobj__18 __pyx_mstate_global->__pyx_codeobj__18
#define __pyx_codeobj__21 __pyx_mstate_global->__pyx_codeobj__21
#define __pyx_codeobj__25 __pyx_mstate_global->__pyx_codeobj__25
/* #### Code section: module_code ### */

/* "vector.from_py":45
 *
 * @cname("__pyx_convert_vector_from_py_double")
 * cdef vector[X] __pyx_convert_vector_from_py_double(object o) except *:             # <<<<<<<<<<<<<<
 *     cdef vector[X] v
 *     for item in o:
 */

static std::vector<double> __pyx_convert_vector_from_py_double(PyObject *__pyx_v_o)
{
    std::vector<double> __pyx_v_v;
    PyObject *__pyx_v_item = NULL;
    std::vector<double> __pyx_r;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    Py_ssize_t __pyx_t_2;
    PyObject *(*__pyx_t_3)(PyObject *);
    PyObject *__pyx_t_4 = NULL;
    double __pyx_t_5;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("__pyx_convert_vector_from_py_double", 1);

    /* "vector.from_py":47
     * cdef vector[X] __pyx_convert_vector_from_py_double(object o) except *:
     *     cdef vector[X] v
     *     for item in o:             # <<<<<<<<<<<<<<
     *         v.push_back(<X>item)
     *     return v
     */
    if (likely(PyList_CheckExact(__pyx_v_o)) || PyTuple_CheckExact(__pyx_v_o))
    {
        __pyx_t_1 = __pyx_v_o;
        __Pyx_INCREF(__pyx_t_1);
        __pyx_t_2 = 0;
        __pyx_t_3 = NULL;
    }
    else
    {
        __pyx_t_2 = -1;
        __pyx_t_1 = PyObject_GetIter(__pyx_v_o);
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(1, 47, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_3 = __Pyx_PyObject_GetIterNextFunc(__pyx_t_1);
        if (unlikely(!__pyx_t_3))
            __PYX_ERR(1, 47, __pyx_L1_error)
    }
    for (;;)
    {
        if (likely(!__pyx_t_3))
        {
            if (likely(PyList_CheckExact(__pyx_t_1)))
            {
                {
                    Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_1);
#if !CYTHON_ASSUME_SAFE_MACROS
                    if (unlikely((__pyx_temp < 0)))
                        __PYX_ERR(1, 47, __pyx_L1_error)
#endif
                    if (__pyx_t_2 >= __pyx_temp)
                        break;
                }
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                __pyx_t_4 = PyList_GET_ITEM(__pyx_t_1, __pyx_t_2);
                __Pyx_INCREF(__pyx_t_4);
                __pyx_t_2++;
                if (unlikely((0 < 0)))
                    __PYX_ERR(1, 47, __pyx_L1_error)
#else
                __pyx_t_4 = __Pyx_PySequence_ITEM(__pyx_t_1, __pyx_t_2);
                __pyx_t_2++;
                if (unlikely(!__pyx_t_4))
                    __PYX_ERR(1, 47, __pyx_L1_error)
                __Pyx_GOTREF(__pyx_t_4);
#endif
            }
            else
            {
                {
                    Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_1);
#if !CYTHON_ASSUME_SAFE_MACROS
                    if (unlikely((__pyx_temp < 0)))
                        __PYX_ERR(1, 47, __pyx_L1_error)
#endif
                    if (__pyx_t_2 >= __pyx_temp)
                        break;
                }
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                __pyx_t_4 = PyTuple_GET_ITEM(__pyx_t_1, __pyx_t_2);
                __Pyx_INCREF(__pyx_t_4);
                __pyx_t_2++;
                if (unlikely((0 < 0)))
                    __PYX_ERR(1, 47, __pyx_L1_error)
#else
                __pyx_t_4 = __Pyx_PySequence_ITEM(__pyx_t_1, __pyx_t_2);
                __pyx_t_2++;
                if (unlikely(!__pyx_t_4))
                    __PYX_ERR(1, 47, __pyx_L1_error)
                __Pyx_GOTREF(__pyx_t_4);
#endif
            }
        }
        else
        {
            __pyx_t_4 = __pyx_t_3(__pyx_t_1);
            if (unlikely(!__pyx_t_4))
            {
                PyObject *exc_type = PyErr_Occurred();
                if (exc_type)
                {
                    if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration)))
                        PyErr_Clear();
                    else
                        __PYX_ERR(1, 47, __pyx_L1_error)
                }
                break;
            }
            __Pyx_GOTREF(__pyx_t_4);
        }
        __Pyx_XDECREF_SET(__pyx_v_item, __pyx_t_4);
        __pyx_t_4 = 0;

        /* "vector.from_py":48
         *     cdef vector[X] v
         *     for item in o:
         *         v.push_back(<X>item)             # <<<<<<<<<<<<<<
         *     return v
         *
         */
        __pyx_t_5 = __pyx_PyFloat_AsDouble(__pyx_v_item);
        if (unlikely((__pyx_t_5 == (double)-1) && PyErr_Occurred()))
            __PYX_ERR(1, 48, __pyx_L1_error)
        try
        {
            __pyx_v_v.push_back(((double)__pyx_t_5));
        }
        catch (...)
        {
            __Pyx_CppExn2PyErr();
            __PYX_ERR(1, 48, __pyx_L1_error)
        }

        /* "vector.from_py":47
         * cdef vector[X] __pyx_convert_vector_from_py_double(object o) except *:
         *     cdef vector[X] v
         *     for item in o:             # <<<<<<<<<<<<<<
         *         v.push_back(<X>item)
         *     return v
         */
    }
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;

    /* "vector.from_py":49
     *     for item in o:
     *         v.push_back(<X>item)
     *     return v             # <<<<<<<<<<<<<<
     *
     *
     */
    __pyx_r = __pyx_v_v;
    goto __pyx_L0;

/* "vector.from_py":45
 *
 * @cname("__pyx_convert_vector_from_py_double")
 * cdef vector[X] __pyx_convert_vector_from_py_double(object o) except *:             # <<<<<<<<<<<<<<
 *     cdef vector[X] v
 *     for item in o:
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_4);
    __Pyx_AddTraceback("vector.from_py.__pyx_convert_vector_from_py_double", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __Pyx_pretend_to_initialize(&__pyx_r);
__pyx_L0:;
    __Pyx_XDECREF(__pyx_v_item);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

static std::vector<std::vector<double>> __pyx_convert_vector_from_py_std_3a__3a_vector_3c_double_3e___(PyObject *__pyx_v_o)
{
    std::vector<std::vector<double>> __pyx_v_v;
    PyObject *__pyx_v_item = NULL;
    std::vector<std::vector<double>> __pyx_r;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    Py_ssize_t __pyx_t_2;
    PyObject *(*__pyx_t_3)(PyObject *);
    PyObject *__pyx_t_4 = NULL;
    std::vector<double> __pyx_t_5;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("__pyx_convert_vector_from_py_std_3a__3a_vector_3c_double_3e___", 1);

    /* "vector.from_py":47
     * cdef vector[X] __pyx_convert_vector_from_py_std_3a__3a_vector_3c_double_3e___(object o) except *:
     *     cdef vector[X] v
     *     for item in o:             # <<<<<<<<<<<<<<
     *         v.push_back(<X>item)
     *     return v
     */
    if (likely(PyList_CheckExact(__pyx_v_o)) || PyTuple_CheckExact(__pyx_v_o))
    {
        __pyx_t_1 = __pyx_v_o;
        __Pyx_INCREF(__pyx_t_1);
        __pyx_t_2 = 0;
        __pyx_t_3 = NULL;
    }
    else
    {
        __pyx_t_2 = -1;
        __pyx_t_1 = PyObject_GetIter(__pyx_v_o);
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(1, 47, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_3 = __Pyx_PyObject_GetIterNextFunc(__pyx_t_1);
        if (unlikely(!__pyx_t_3))
            __PYX_ERR(1, 47, __pyx_L1_error)
    }
    for (;;)
    {
        if (likely(!__pyx_t_3))
        {
            if (likely(PyList_CheckExact(__pyx_t_1)))
            {
                {
                    Py_ssize_t __pyx_temp = __Pyx_PyList_GET_SIZE(__pyx_t_1);
#if !CYTHON_ASSUME_SAFE_MACROS
                    if (unlikely((__pyx_temp < 0)))
                        __PYX_ERR(1, 47, __pyx_L1_error)
#endif
                    if (__pyx_t_2 >= __pyx_temp)
                        break;
                }
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                __pyx_t_4 = PyList_GET_ITEM(__pyx_t_1, __pyx_t_2);
                __Pyx_INCREF(__pyx_t_4);
                __pyx_t_2++;
                if (unlikely((0 < 0)))
                    __PYX_ERR(1, 47, __pyx_L1_error)
#else
                __pyx_t_4 = __Pyx_PySequence_ITEM(__pyx_t_1, __pyx_t_2);
                __pyx_t_2++;
                if (unlikely(!__pyx_t_4))
                    __PYX_ERR(1, 47, __pyx_L1_error)
                __Pyx_GOTREF(__pyx_t_4);
#endif
            }
            else
            {
                {
                    Py_ssize_t __pyx_temp = __Pyx_PyTuple_GET_SIZE(__pyx_t_1);
#if !CYTHON_ASSUME_SAFE_MACROS
                    if (unlikely((__pyx_temp < 0)))
                        __PYX_ERR(1, 47, __pyx_L1_error)
#endif
                    if (__pyx_t_2 >= __pyx_temp)
                        break;
                }
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                __pyx_t_4 = PyTuple_GET_ITEM(__pyx_t_1, __pyx_t_2);
                __Pyx_INCREF(__pyx_t_4);
                __pyx_t_2++;
                if (unlikely((0 < 0)))
                    __PYX_ERR(1, 47, __pyx_L1_error)
#else
                __pyx_t_4 = __Pyx_PySequence_ITEM(__pyx_t_1, __pyx_t_2);
                __pyx_t_2++;
                if (unlikely(!__pyx_t_4))
                    __PYX_ERR(1, 47, __pyx_L1_error)
                __Pyx_GOTREF(__pyx_t_4);
#endif
            }
        }
        else
        {
            __pyx_t_4 = __pyx_t_3(__pyx_t_1);
            if (unlikely(!__pyx_t_4))
            {
                PyObject *exc_type = PyErr_Occurred();
                if (exc_type)
                {
                    if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration)))
                        PyErr_Clear();
                    else
                        __PYX_ERR(1, 47, __pyx_L1_error)
                }
                break;
            }
            __Pyx_GOTREF(__pyx_t_4);
        }
        __Pyx_XDECREF_SET(__pyx_v_item, __pyx_t_4);
        __pyx_t_4 = 0;

        /* "vector.from_py":48
         *     cdef vector[X] v
         *     for item in o:
         *         v.push_back(<X>item)             # <<<<<<<<<<<<<<
         *     return v
         *
         */
        __pyx_t_5 = __pyx_convert_vector_from_py_double(__pyx_v_item);
        if (unlikely(PyErr_Occurred()))
            __PYX_ERR(1, 48, __pyx_L1_error)
        try
        {
            __pyx_v_v.push_back(((std::vector<double>)__pyx_t_5));
        }
        catch (...)
        {
            __Pyx_CppExn2PyErr();
            __PYX_ERR(1, 48, __pyx_L1_error)
        }

        /* "vector.from_py":47
         * cdef vector[X] __pyx_convert_vector_from_py_std_3a__3a_vector_3c_double_3e___(object o) except *:
         *     cdef vector[X] v
         *     for item in o:             # <<<<<<<<<<<<<<
         *         v.push_back(<X>item)
         *     return v
         */
    }
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;

    /* "vector.from_py":49
     *     for item in o:
     *         v.push_back(<X>item)
     *     return v             # <<<<<<<<<<<<<<
     *
     *
     */
    __pyx_r = __pyx_v_v;
    goto __pyx_L0;

/* "vector.from_py":45
 *
 * @cname("__pyx_convert_vector_from_py_std_3a__3a_vector_3c_double_3e___")
 * cdef vector[X] __pyx_convert_vector_from_py_std_3a__3a_vector_3c_double_3e___(object o) except *:             # <<<<<<<<<<<<<<
 *     cdef vector[X] v
 *     for item in o:
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_4);
    __Pyx_AddTraceback("vector.from_py.__pyx_convert_vector_from_py_std_3a__3a_vector_3c_double_3e___", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __Pyx_pretend_to_initialize(&__pyx_r);
__pyx_L0:;
    __Pyx_XDECREF(__pyx_v_item);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "vector.to_py":66
 *
 * @cname("__pyx_convert_vector_to_py_double")
 * cdef object __pyx_convert_vector_to_py_double(const vector[X]& v):             # <<<<<<<<<<<<<<
 *     if v.size() > <size_t> PY_SSIZE_T_MAX:
 *         raise MemoryError()
 */

static PyObject *__pyx_convert_vector_to_py_double(std::vector<double> const &__pyx_v_v)
{
    Py_ssize_t __pyx_v_v_size_signed;
    PyObject *__pyx_v_o = NULL;
    Py_ssize_t __pyx_v_i;
    PyObject *__pyx_v_item = 0;
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations int __pyx_t_1;
    PyObject *__pyx_t_2 = NULL;
    Py_ssize_t __pyx_t_3;
    Py_ssize_t __pyx_t_4;
    Py_ssize_t __pyx_t_5;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("__pyx_convert_vector_to_py_double", 1);

    /* "vector.to_py":67
     * @cname("__pyx_convert_vector_to_py_double")
     * cdef object __pyx_convert_vector_to_py_double(const vector[X]& v):
     *     if v.size() > <size_t> PY_SSIZE_T_MAX:             # <<<<<<<<<<<<<<
     *         raise MemoryError()
     *     v_size_signed = <Py_ssize_t> v.size()
     */
    __pyx_t_1 = (__pyx_v_v.size() > ((size_t)PY_SSIZE_T_MAX));
    if (unlikely(__pyx_t_1))
    {

        /* "vector.to_py":68
         * cdef object __pyx_convert_vector_to_py_double(const vector[X]& v):
         *     if v.size() > <size_t> PY_SSIZE_T_MAX:
         *         raise MemoryError()             # <<<<<<<<<<<<<<
         *     v_size_signed = <Py_ssize_t> v.size()
         *
         */
        PyErr_NoMemory();
        __PYX_ERR(1, 68, __pyx_L1_error)

        /* "vector.to_py":67
         * @cname("__pyx_convert_vector_to_py_double")
         * cdef object __pyx_convert_vector_to_py_double(const vector[X]& v):
         *     if v.size() > <size_t> PY_SSIZE_T_MAX:             # <<<<<<<<<<<<<<
         *         raise MemoryError()
         *     v_size_signed = <Py_ssize_t> v.size()
         */
    }

    /* "vector.to_py":69
     *     if v.size() > <size_t> PY_SSIZE_T_MAX:
     *         raise MemoryError()
     *     v_size_signed = <Py_ssize_t> v.size()             # <<<<<<<<<<<<<<
     *
     *     o = PyList_New(v_size_signed)
     */
    __pyx_v_v_size_signed = ((Py_ssize_t)__pyx_v_v.size());

    /* "vector.to_py":71
     *     v_size_signed = <Py_ssize_t> v.size()
     *
     *     o = PyList_New(v_size_signed)             # <<<<<<<<<<<<<<
     *
     *     cdef Py_ssize_t i
     */
    __pyx_t_2 = PyList_New(__pyx_v_v_size_signed);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(1, 71, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_v_o = ((PyObject *)__pyx_t_2);
    __pyx_t_2 = 0;

    /* "vector.to_py":76
     *     cdef object item
     *
     *     for i in range(v_size_signed):             # <<<<<<<<<<<<<<
     *         item = v[i]
     *         Py_INCREF(item)
     */
    __pyx_t_3 = __pyx_v_v_size_signed;
    __pyx_t_4 = __pyx_t_3;
    for (__pyx_t_5 = 0; __pyx_t_5 < __pyx_t_4; __pyx_t_5 += 1)
    {
        __pyx_v_i = __pyx_t_5;

        /* "vector.to_py":77
         *
         *     for i in range(v_size_signed):
         *         item = v[i]             # <<<<<<<<<<<<<<
         *         Py_INCREF(item)
         *         PyList_SET_ITEM(o, i, item)
         */
        __pyx_t_2 = PyFloat_FromDouble((__pyx_v_v[__pyx_v_i]));
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(1, 77, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_XDECREF_SET(__pyx_v_item, __pyx_t_2);
        __pyx_t_2 = 0;

        /* "vector.to_py":78
         *     for i in range(v_size_signed):
         *         item = v[i]
         *         Py_INCREF(item)             # <<<<<<<<<<<<<<
         *         PyList_SET_ITEM(o, i, item)
         *
         */
        Py_INCREF(__pyx_v_item);

        /* "vector.to_py":79
         *         item = v[i]
         *         Py_INCREF(item)
         *         PyList_SET_ITEM(o, i, item)             # <<<<<<<<<<<<<<
         *
         *     return o
         */
        PyList_SET_ITEM(__pyx_v_o, __pyx_v_i, __pyx_v_item);
    }

    /* "vector.to_py":81
     *         PyList_SET_ITEM(o, i, item)
     *
     *     return o             # <<<<<<<<<<<<<<
     *
     */
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_o);
    __pyx_r = __pyx_v_o;
    goto __pyx_L0;

/* "vector.to_py":66
 *
 * @cname("__pyx_convert_vector_to_py_double")
 * cdef object __pyx_convert_vector_to_py_double(const vector[X]& v):             # <<<<<<<<<<<<<<
 *     if v.size() > <size_t> PY_SSIZE_T_MAX:
 *         raise MemoryError()
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_AddTraceback("vector.to_py.__pyx_convert_vector_to_py_double", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = 0;
__pyx_L0:;
    __Pyx_XDECREF(__pyx_v_o);
    __Pyx_XDECREF(__pyx_v_item);
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

static PyObject *__pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___(std::vector<std::vector<double>> const &__pyx_v_v)
{
    Py_ssize_t __pyx_v_v_size_signed;
    PyObject *__pyx_v_o = NULL;
    Py_ssize_t __pyx_v_i;
    PyObject *__pyx_v_item = 0;
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations int __pyx_t_1;
    PyObject *__pyx_t_2 = NULL;
    Py_ssize_t __pyx_t_3;
    Py_ssize_t __pyx_t_4;
    Py_ssize_t __pyx_t_5;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("__pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___", 1);

    /* "vector.to_py":67
     * @cname("__pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___")
     * cdef object __pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___(const vector[X]& v):
     *     if v.size() > <size_t> PY_SSIZE_T_MAX:             # <<<<<<<<<<<<<<
     *         raise MemoryError()
     *     v_size_signed = <Py_ssize_t> v.size()
     */
    __pyx_t_1 = (__pyx_v_v.size() > ((size_t)PY_SSIZE_T_MAX));
    if (unlikely(__pyx_t_1))
    {

        /* "vector.to_py":68
         * cdef object __pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___(const vector[X]& v):
         *     if v.size() > <size_t> PY_SSIZE_T_MAX:
         *         raise MemoryError()             # <<<<<<<<<<<<<<
         *     v_size_signed = <Py_ssize_t> v.size()
         *
         */
        PyErr_NoMemory();
        __PYX_ERR(1, 68, __pyx_L1_error)

        /* "vector.to_py":67
         * @cname("__pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___")
         * cdef object __pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___(const vector[X]& v):
         *     if v.size() > <size_t> PY_SSIZE_T_MAX:             # <<<<<<<<<<<<<<
         *         raise MemoryError()
         *     v_size_signed = <Py_ssize_t> v.size()
         */
    }

    /* "vector.to_py":69
     *     if v.size() > <size_t> PY_SSIZE_T_MAX:
     *         raise MemoryError()
     *     v_size_signed = <Py_ssize_t> v.size()             # <<<<<<<<<<<<<<
     *
     *     o = PyList_New(v_size_signed)
     */
    __pyx_v_v_size_signed = ((Py_ssize_t)__pyx_v_v.size());

    /* "vector.to_py":71
     *     v_size_signed = <Py_ssize_t> v.size()
     *
     *     o = PyList_New(v_size_signed)             # <<<<<<<<<<<<<<
     *
     *     cdef Py_ssize_t i
     */
    __pyx_t_2 = PyList_New(__pyx_v_v_size_signed);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(1, 71, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_v_o = ((PyObject *)__pyx_t_2);
    __pyx_t_2 = 0;

    /* "vector.to_py":76
     *     cdef object item
     *
     *     for i in range(v_size_signed):             # <<<<<<<<<<<<<<
     *         item = v[i]
     *         Py_INCREF(item)
     */
    __pyx_t_3 = __pyx_v_v_size_signed;
    __pyx_t_4 = __pyx_t_3;
    for (__pyx_t_5 = 0; __pyx_t_5 < __pyx_t_4; __pyx_t_5 += 1)
    {
        __pyx_v_i = __pyx_t_5;

        /* "vector.to_py":77
         *
         *     for i in range(v_size_signed):
         *         item = v[i]             # <<<<<<<<<<<<<<
         *         Py_INCREF(item)
         *         PyList_SET_ITEM(o, i, item)
         */
        __pyx_t_2 = __pyx_convert_vector_to_py_double((__pyx_v_v[__pyx_v_i]));
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(1, 77, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_XDECREF_SET(__pyx_v_item, __pyx_t_2);
        __pyx_t_2 = 0;

        /* "vector.to_py":78
         *     for i in range(v_size_signed):
         *         item = v[i]
         *         Py_INCREF(item)             # <<<<<<<<<<<<<<
         *         PyList_SET_ITEM(o, i, item)
         *
         */
        Py_INCREF(__pyx_v_item);

        /* "vector.to_py":79
         *         item = v[i]
         *         Py_INCREF(item)
         *         PyList_SET_ITEM(o, i, item)             # <<<<<<<<<<<<<<
         *
         *     return o
         */
        PyList_SET_ITEM(__pyx_v_o, __pyx_v_i, __pyx_v_item);
    }

    /* "vector.to_py":81
     *         PyList_SET_ITEM(o, i, item)
     *
     *     return o             # <<<<<<<<<<<<<<
     *
     */
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_o);
    __pyx_r = __pyx_v_o;
    goto __pyx_L0;

/* "vector.to_py":66
 *
 * @cname("__pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___")
 * cdef object __pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___(const vector[X]& v):             # <<<<<<<<<<<<<<
 *     if v.size() > <size_t> PY_SSIZE_T_MAX:
 *         raise MemoryError()
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_AddTraceback("vector.to_py.__pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = 0;
__pyx_L0:;
    __Pyx_XDECREF(__pyx_v_o);
    __Pyx_XDECREF(__pyx_v_item);
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "pair.to_py":190
 *
 * @cname("__pyx_convert_pair_to_py_double____std_3a__3a_vector_3c_std_3a__3a_vector_3c_double_3e____3e___")
 * cdef object __pyx_convert_pair_to_py_double____std_3a__3a_vector_3c_std_3a__3a_vector_3c_double_3e____3e___(const pair[X,Y]& p):             # <<<<<<<<<<<<<<
 *     return p.first, p.second
 *
 */

static PyObject *__pyx_convert_pair_to_py_double____std_3a__3a_vector_3c_std_3a__3a_vector_3c_double_3e____3e___(std::pair<double, std::vector<std::vector<double>>> const &__pyx_v_p)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("__pyx_convert_pair_to_py_double____std_3a__3a_vector_3c_std_3a__3a_vector_3c_double_3e____3e___", 1);

    /* "pair.to_py":191
     * @cname("__pyx_convert_pair_to_py_double____std_3a__3a_vector_3c_std_3a__3a_vector_3c_double_3e____3e___")
     * cdef object __pyx_convert_pair_to_py_double____std_3a__3a_vector_3c_std_3a__3a_vector_3c_double_3e____3e___(const pair[X,Y]& p):
     *     return p.first, p.second             # <<<<<<<<<<<<<<
     *
     *
     */
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_1 = PyFloat_FromDouble(__pyx_v_p.first);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(1, 191, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __pyx_convert_vector_to_py_std_3a__3a_vector_3c_double_3e___(__pyx_v_p.second);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(1, 191, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = PyTuple_New(2);
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(1, 191, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_1);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_1))
        __PYX_ERR(1, 191, __pyx_L1_error);
    __Pyx_GIVEREF(__pyx_t_2);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_t_2))
        __PYX_ERR(1, 191, __pyx_L1_error);
    __pyx_t_1 = 0;
    __pyx_t_2 = 0;
    __pyx_r = __pyx_t_3;
    __pyx_t_3 = 0;
    goto __pyx_L0;

/* "pair.to_py":190
 *
 * @cname("__pyx_convert_pair_to_py_double____std_3a__3a_vector_3c_std_3a__3a_vector_3c_double_3e____3e___")
 * cdef object __pyx_convert_pair_to_py_double____std_3a__3a_vector_3c_std_3a__3a_vector_3c_double_3e____3e___(const pair[X,Y]& p):             # <<<<<<<<<<<<<<
 *     return p.first, p.second
 *
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_3);
    __Pyx_AddTraceback("pair.to_py.__pyx_convert_pair_to_py_double____std_3a__3a_vector_3c_std_3a__3a_vector_3c_double_3e____3e___", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = 0;
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":245
 *
 *         @property
 *         cdef inline PyObject* base(self) nogil:             # <<<<<<<<<<<<<<
 *             """Returns a borrowed reference to the object owning the data/memory.
 *             """
 */

static CYTHON_INLINE PyObject *__pyx_f_5numpy_7ndarray_4base_base(PyArrayObject *__pyx_v_self)
{
    PyObject *__pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":248
     *             """Returns a borrowed reference to the object owning the data/memory.
     *             """
     *             return PyArray_BASE(self)             # <<<<<<<<<<<<<<
     *
     *         @property
     */
    __pyx_r = PyArray_BASE(__pyx_v_self);
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":245
 *
 *         @property
 *         cdef inline PyObject* base(self) nogil:             # <<<<<<<<<<<<<<
 *             """Returns a borrowed reference to the object owning the data/memory.
 *             """
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":251
 *
 *         @property
 *         cdef inline dtype descr(self):             # <<<<<<<<<<<<<<
 *             """Returns an owned reference to the dtype of the array.
 *             """
 */

static CYTHON_INLINE PyArray_Descr *__pyx_f_5numpy_7ndarray_5descr_descr(PyArrayObject *__pyx_v_self)
{
    PyArray_Descr *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyArray_Descr *__pyx_t_1;
    __Pyx_RefNannySetupContext("descr", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":254
     *             """Returns an owned reference to the dtype of the array.
     *             """
     *             return <dtype>PyArray_DESCR(self)             # <<<<<<<<<<<<<<
     *
     *         @property
     */
    __Pyx_XDECREF((PyObject *)__pyx_r);
    __pyx_t_1 = PyArray_DESCR(__pyx_v_self);
    __Pyx_INCREF((PyObject *)((PyArray_Descr *)__pyx_t_1));
    __pyx_r = ((PyArray_Descr *)__pyx_t_1);
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":251
 *
 *         @property
 *         cdef inline dtype descr(self):             # <<<<<<<<<<<<<<
 *             """Returns an owned reference to the dtype of the array.
 *             """
 */

/* function exit code */
__pyx_L0:;
    __Pyx_XGIVEREF((PyObject *)__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":257
 *
 *         @property
 *         cdef inline int ndim(self) nogil:             # <<<<<<<<<<<<<<
 *             """Returns the number of dimensions in the array.
 *             """
 */

static CYTHON_INLINE int __pyx_f_5numpy_7ndarray_4ndim_ndim(PyArrayObject *__pyx_v_self)
{
    int __pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":260
     *             """Returns the number of dimensions in the array.
     *             """
     *             return PyArray_NDIM(self)             # <<<<<<<<<<<<<<
     *
     *         @property
     */
    __pyx_r = PyArray_NDIM(__pyx_v_self);
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":257
 *
 *         @property
 *         cdef inline int ndim(self) nogil:             # <<<<<<<<<<<<<<
 *             """Returns the number of dimensions in the array.
 *             """
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":263
 *
 *         @property
 *         cdef inline npy_intp *shape(self) nogil:             # <<<<<<<<<<<<<<
 *             """Returns a pointer to the dimensions/shape of the array.
 *             The number of elements matches the number of dimensions of the array (ndim).
 */

static CYTHON_INLINE npy_intp *__pyx_f_5numpy_7ndarray_5shape_shape(PyArrayObject *__pyx_v_self)
{
    npy_intp *__pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":268
     *             Can return NULL for 0-dimensional arrays.
     *             """
     *             return PyArray_DIMS(self)             # <<<<<<<<<<<<<<
     *
     *         @property
     */
    __pyx_r = PyArray_DIMS(__pyx_v_self);
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":263
 *
 *         @property
 *         cdef inline npy_intp *shape(self) nogil:             # <<<<<<<<<<<<<<
 *             """Returns a pointer to the dimensions/shape of the array.
 *             The number of elements matches the number of dimensions of the array (ndim).
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":271
 *
 *         @property
 *         cdef inline npy_intp *strides(self) nogil:             # <<<<<<<<<<<<<<
 *             """Returns a pointer to the strides of the array.
 *             The number of elements matches the number of dimensions of the array (ndim).
 */

static CYTHON_INLINE npy_intp *__pyx_f_5numpy_7ndarray_7strides_strides(PyArrayObject *__pyx_v_self)
{
    npy_intp *__pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":275
     *             The number of elements matches the number of dimensions of the array (ndim).
     *             """
     *             return PyArray_STRIDES(self)             # <<<<<<<<<<<<<<
     *
     *         @property
     */
    __pyx_r = PyArray_STRIDES(__pyx_v_self);
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":271
 *
 *         @property
 *         cdef inline npy_intp *strides(self) nogil:             # <<<<<<<<<<<<<<
 *             """Returns a pointer to the strides of the array.
 *             The number of elements matches the number of dimensions of the array (ndim).
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":278
 *
 *         @property
 *         cdef inline npy_intp size(self) nogil:             # <<<<<<<<<<<<<<
 *             """Returns the total size (in number of elements) of the array.
 *             """
 */

static CYTHON_INLINE npy_intp __pyx_f_5numpy_7ndarray_4size_size(PyArrayObject *__pyx_v_self)
{
    npy_intp __pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":281
     *             """Returns the total size (in number of elements) of the array.
     *             """
     *             return PyArray_SIZE(self)             # <<<<<<<<<<<<<<
     *
     *         @property
     */
    __pyx_r = PyArray_SIZE(__pyx_v_self);
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":278
 *
 *         @property
 *         cdef inline npy_intp size(self) nogil:             # <<<<<<<<<<<<<<
 *             """Returns the total size (in number of elements) of the array.
 *             """
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":284
 *
 *         @property
 *         cdef inline char* data(self) nogil:             # <<<<<<<<<<<<<<
 *             """The pointer to the data buffer as a char*.
 *             This is provided for legacy reasons to avoid direct struct field access.
 */

static CYTHON_INLINE char *__pyx_f_5numpy_7ndarray_4data_data(PyArrayObject *__pyx_v_self)
{
    char *__pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":290
     *             of `PyArray_DATA()` instead, which returns a 'void*'.
     *             """
     *             return PyArray_BYTES(self)             # <<<<<<<<<<<<<<
     *
     *     ctypedef unsigned char      npy_bool
     */
    __pyx_r = PyArray_BYTES(__pyx_v_self);
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":284
 *
 *         @property
 *         cdef inline char* data(self) nogil:             # <<<<<<<<<<<<<<
 *             """The pointer to the data buffer as a char*.
 *             This is provided for legacy reasons to avoid direct struct field access.
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":773
 * ctypedef npy_cdouble     complex_t
 *
 * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
 *     return PyArray_MultiIterNew(1, <void*>a)
 *
 */

static CYTHON_INLINE PyObject *__pyx_f_5numpy_PyArray_MultiIterNew1(PyObject *__pyx_v_a)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("PyArray_MultiIterNew1", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":774
     *
     * cdef inline object PyArray_MultiIterNew1(a):
     *     return PyArray_MultiIterNew(1, <void*>a)             # <<<<<<<<<<<<<<
     *
     * cdef inline object PyArray_MultiIterNew2(a, b):
     */
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_1 = PyArray_MultiIterNew(1, ((void *)__pyx_v_a));
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(2, 774, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_r = __pyx_t_1;
    __pyx_t_1 = 0;
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":773
 * ctypedef npy_cdouble     complex_t
 *
 * cdef inline object PyArray_MultiIterNew1(a):             # <<<<<<<<<<<<<<
 *     return PyArray_MultiIterNew(1, <void*>a)
 *
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_AddTraceback("numpy.PyArray_MultiIterNew1", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = 0;
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":776
 *     return PyArray_MultiIterNew(1, <void*>a)
 *
 * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
 *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
 *
 */

static CYTHON_INLINE PyObject *__pyx_f_5numpy_PyArray_MultiIterNew2(PyObject *__pyx_v_a, PyObject *__pyx_v_b)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("PyArray_MultiIterNew2", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":777
     *
     * cdef inline object PyArray_MultiIterNew2(a, b):
     *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)             # <<<<<<<<<<<<<<
     *
     * cdef inline object PyArray_MultiIterNew3(a, b, c):
     */
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_1 = PyArray_MultiIterNew(2, ((void *)__pyx_v_a), ((void *)__pyx_v_b));
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(2, 777, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_r = __pyx_t_1;
    __pyx_t_1 = 0;
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":776
 *     return PyArray_MultiIterNew(1, <void*>a)
 *
 * cdef inline object PyArray_MultiIterNew2(a, b):             # <<<<<<<<<<<<<<
 *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
 *
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_AddTraceback("numpy.PyArray_MultiIterNew2", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = 0;
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":779
 *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
 *
 * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
 *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
 *
 */

static CYTHON_INLINE PyObject *__pyx_f_5numpy_PyArray_MultiIterNew3(PyObject *__pyx_v_a, PyObject *__pyx_v_b, PyObject *__pyx_v_c)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("PyArray_MultiIterNew3", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":780
     *
     * cdef inline object PyArray_MultiIterNew3(a, b, c):
     *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)             # <<<<<<<<<<<<<<
     *
     * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
     */
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_1 = PyArray_MultiIterNew(3, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c));
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(2, 780, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_r = __pyx_t_1;
    __pyx_t_1 = 0;
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":779
 *     return PyArray_MultiIterNew(2, <void*>a, <void*>b)
 *
 * cdef inline object PyArray_MultiIterNew3(a, b, c):             # <<<<<<<<<<<<<<
 *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
 *
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_AddTraceback("numpy.PyArray_MultiIterNew3", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = 0;
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":782
 *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
 *
 * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
 *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
 *
 */

static CYTHON_INLINE PyObject *__pyx_f_5numpy_PyArray_MultiIterNew4(PyObject *__pyx_v_a, PyObject *__pyx_v_b, PyObject *__pyx_v_c, PyObject *__pyx_v_d)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("PyArray_MultiIterNew4", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":783
     *
     * cdef inline object PyArray_MultiIterNew4(a, b, c, d):
     *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)             # <<<<<<<<<<<<<<
     *
     * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
     */
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_1 = PyArray_MultiIterNew(4, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d));
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(2, 783, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_r = __pyx_t_1;
    __pyx_t_1 = 0;
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":782
 *     return PyArray_MultiIterNew(3, <void*>a, <void*>b, <void*> c)
 *
 * cdef inline object PyArray_MultiIterNew4(a, b, c, d):             # <<<<<<<<<<<<<<
 *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
 *
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_AddTraceback("numpy.PyArray_MultiIterNew4", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = 0;
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":785
 *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
 *
 * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
 *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
 *
 */

static CYTHON_INLINE PyObject *__pyx_f_5numpy_PyArray_MultiIterNew5(PyObject *__pyx_v_a, PyObject *__pyx_v_b, PyObject *__pyx_v_c, PyObject *__pyx_v_d, PyObject *__pyx_v_e)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("PyArray_MultiIterNew5", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":786
     *
     * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):
     *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)             # <<<<<<<<<<<<<<
     *
     * cdef inline tuple PyDataType_SHAPE(dtype d):
     */
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_1 = PyArray_MultiIterNew(5, ((void *)__pyx_v_a), ((void *)__pyx_v_b), ((void *)__pyx_v_c), ((void *)__pyx_v_d), ((void *)__pyx_v_e));
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(2, 786, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_r = __pyx_t_1;
    __pyx_t_1 = 0;
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":785
 *     return PyArray_MultiIterNew(4, <void*>a, <void*>b, <void*>c, <void*> d)
 *
 * cdef inline object PyArray_MultiIterNew5(a, b, c, d, e):             # <<<<<<<<<<<<<<
 *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
 *
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_AddTraceback("numpy.PyArray_MultiIterNew5", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = 0;
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":788
 *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
 *
 * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
 *     if PyDataType_HASSUBARRAY(d):
 *         return <tuple>d.subarray.shape
 */

static CYTHON_INLINE PyObject *__pyx_f_5numpy_PyDataType_SHAPE(PyArray_Descr *__pyx_v_d)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations int __pyx_t_1;
    __Pyx_RefNannySetupContext("PyDataType_SHAPE", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":789
     *
     * cdef inline tuple PyDataType_SHAPE(dtype d):
     *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
     *         return <tuple>d.subarray.shape
     *     else:
     */
    __pyx_t_1 = PyDataType_HASSUBARRAY(__pyx_v_d);
    if (__pyx_t_1)
    {

        /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":790
         * cdef inline tuple PyDataType_SHAPE(dtype d):
         *     if PyDataType_HASSUBARRAY(d):
         *         return <tuple>d.subarray.shape             # <<<<<<<<<<<<<<
         *     else:
         *         return ()
         */
        __Pyx_XDECREF(__pyx_r);
        __Pyx_INCREF(((PyObject *)__pyx_v_d->subarray->shape));
        __pyx_r = ((PyObject *)__pyx_v_d->subarray->shape);
        goto __pyx_L0;

        /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":789
         *
         * cdef inline tuple PyDataType_SHAPE(dtype d):
         *     if PyDataType_HASSUBARRAY(d):             # <<<<<<<<<<<<<<
         *         return <tuple>d.subarray.shape
         *     else:
         */
    }

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":792
     *         return <tuple>d.subarray.shape
     *     else:
     *         return ()             # <<<<<<<<<<<<<<
     *
     *
     */
    /*else*/ {
        __Pyx_XDECREF(__pyx_r);
        __Pyx_INCREF(__pyx_empty_tuple);
        __pyx_r = __pyx_empty_tuple;
        goto __pyx_L0;
    }

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":788
 *     return PyArray_MultiIterNew(5, <void*>a, <void*>b, <void*>c, <void*> d, <void*> e)
 *
 * cdef inline tuple PyDataType_SHAPE(dtype d):             # <<<<<<<<<<<<<<
 *     if PyDataType_HASSUBARRAY(d):
 *         return <tuple>d.subarray.shape
 */

/* function exit code */
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":968
 *     int _import_umath() except -1
 *
 * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
 *     Py_INCREF(base) # important to do this before stealing the reference below!
 *     PyArray_SetBaseObject(arr, base)
 */

static CYTHON_INLINE void __pyx_f_5numpy_set_array_base(PyArrayObject *__pyx_v_arr, PyObject *__pyx_v_base)
{
    int __pyx_t_1;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":969
     *
     * cdef inline void set_array_base(ndarray arr, object base):
     *     Py_INCREF(base) # important to do this before stealing the reference below!             # <<<<<<<<<<<<<<
     *     PyArray_SetBaseObject(arr, base)
     *
     */
    Py_INCREF(__pyx_v_base);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":970
     * cdef inline void set_array_base(ndarray arr, object base):
     *     Py_INCREF(base) # important to do this before stealing the reference below!
     *     PyArray_SetBaseObject(arr, base)             # <<<<<<<<<<<<<<
     *
     * cdef inline object get_array_base(ndarray arr):
     */
    __pyx_t_1 = PyArray_SetBaseObject(__pyx_v_arr, __pyx_v_base);
    if (unlikely(__pyx_t_1 == ((int)-1)))
        __PYX_ERR(2, 970, __pyx_L1_error)

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":968
     *     int _import_umath() except -1
     *
     * cdef inline void set_array_base(ndarray arr, object base):             # <<<<<<<<<<<<<<
     *     Py_INCREF(base) # important to do this before stealing the reference below!
     *     PyArray_SetBaseObject(arr, base)
     */

    /* function exit code */
    goto __pyx_L0;
__pyx_L1_error:;
    __Pyx_AddTraceback("numpy.set_array_base", __pyx_clineno, __pyx_lineno, __pyx_filename);
__pyx_L0:;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":972
 *     PyArray_SetBaseObject(arr, base)
 *
 * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
 *     base = PyArray_BASE(arr)
 *     if base is NULL:
 */

static CYTHON_INLINE PyObject *__pyx_f_5numpy_get_array_base(PyArrayObject *__pyx_v_arr)
{
    PyObject *__pyx_v_base;
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations int __pyx_t_1;
    __Pyx_RefNannySetupContext("get_array_base", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":973
     *
     * cdef inline object get_array_base(ndarray arr):
     *     base = PyArray_BASE(arr)             # <<<<<<<<<<<<<<
     *     if base is NULL:
     *         return None
     */
    __pyx_v_base = PyArray_BASE(__pyx_v_arr);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":974
     * cdef inline object get_array_base(ndarray arr):
     *     base = PyArray_BASE(arr)
     *     if base is NULL:             # <<<<<<<<<<<<<<
     *         return None
     *     return <object>base
     */
    __pyx_t_1 = (__pyx_v_base == NULL);
    if (__pyx_t_1)
    {

        /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":975
         *     base = PyArray_BASE(arr)
         *     if base is NULL:
         *         return None             # <<<<<<<<<<<<<<
         *     return <object>base
         *
         */
        __Pyx_XDECREF(__pyx_r);
        __pyx_r = Py_None;
        __Pyx_INCREF(Py_None);
        goto __pyx_L0;

        /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":974
         * cdef inline object get_array_base(ndarray arr):
         *     base = PyArray_BASE(arr)
         *     if base is NULL:             # <<<<<<<<<<<<<<
         *         return None
         *     return <object>base
         */
    }

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":976
     *     if base is NULL:
     *         return None
     *     return <object>base             # <<<<<<<<<<<<<<
     *
     * # Versions of the import_* functions which are more suitable for
     */
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(((PyObject *)__pyx_v_base));
    __pyx_r = ((PyObject *)__pyx_v_base);
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":972
 *     PyArray_SetBaseObject(arr, base)
 *
 * cdef inline object get_array_base(ndarray arr):             # <<<<<<<<<<<<<<
 *     base = PyArray_BASE(arr)
 *     if base is NULL:
 */

/* function exit code */
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":980
 * # Versions of the import_* functions which are more suitable for
 * # Cython code.
 * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
 *     try:
 *         __pyx_import_array()
 */

static CYTHON_INLINE int __pyx_f_5numpy_import_array(void)
{
    int __pyx_r;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    int __pyx_t_4;
    PyObject *__pyx_t_5 = NULL;
    PyObject *__pyx_t_6 = NULL;
    PyObject *__pyx_t_7 = NULL;
    PyObject *__pyx_t_8 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("import_array", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":981
     * # Cython code.
     * cdef inline int import_array() except -1:
     *     try:             # <<<<<<<<<<<<<<
     *         __pyx_import_array()
     *     except Exception:
     */
    {
        __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
                __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
        __Pyx_XGOTREF(__pyx_t_1);
        __Pyx_XGOTREF(__pyx_t_2);
        __Pyx_XGOTREF(__pyx_t_3);
        /*try:*/ {

            /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":982
             * cdef inline int import_array() except -1:
             *     try:
             *         __pyx_import_array()             # <<<<<<<<<<<<<<
             *     except Exception:
             *         raise ImportError("numpy.core.multiarray failed to import")
             */
            __pyx_t_4 = _import_array();
            if (unlikely(__pyx_t_4 == ((int)-1)))
                __PYX_ERR(2, 982, __pyx_L3_error)

            /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":981
             * # Cython code.
             * cdef inline int import_array() except -1:
             *     try:             # <<<<<<<<<<<<<<
             *         __pyx_import_array()
             *     except Exception:
             */
        }
        __Pyx_XDECREF(__pyx_t_1);
        __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        goto __pyx_L8_try_end;
    __pyx_L3_error:;

        /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":983
         *     try:
         *         __pyx_import_array()
         *     except Exception:             # <<<<<<<<<<<<<<
         *         raise ImportError("numpy.core.multiarray failed to import")
         *
         */
        __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject *)PyExc_Exception)[0])));
        if (__pyx_t_4)
        {
            __Pyx_AddTraceback("numpy.import_array", __pyx_clineno, __pyx_lineno, __pyx_filename);
            if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0)
                __PYX_ERR(2, 983, __pyx_L5_except_error)
            __Pyx_XGOTREF(__pyx_t_5);
            __Pyx_XGOTREF(__pyx_t_6);
            __Pyx_XGOTREF(__pyx_t_7);

            /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":984
             *         __pyx_import_array()
             *     except Exception:
             *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
             *
             * cdef inline int import_umath() except -1:
             */
            __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_ImportError, __pyx_tuple_, NULL);
            if (unlikely(!__pyx_t_8))
                __PYX_ERR(2, 984, __pyx_L5_except_error)
            __Pyx_GOTREF(__pyx_t_8);
            __Pyx_Raise(__pyx_t_8, 0, 0, 0);
            __Pyx_DECREF(__pyx_t_8);
            __pyx_t_8 = 0;
            __PYX_ERR(2, 984, __pyx_L5_except_error)
        }
        goto __pyx_L5_except_error;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":981
     * # Cython code.
     * cdef inline int import_array() except -1:
     *     try:             # <<<<<<<<<<<<<<
     *         __pyx_import_array()
     *     except Exception:
     */
    __pyx_L5_except_error:;
        __Pyx_XGIVEREF(__pyx_t_1);
        __Pyx_XGIVEREF(__pyx_t_2);
        __Pyx_XGIVEREF(__pyx_t_3);
        __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
        goto __pyx_L1_error;
    __pyx_L8_try_end:;
    }

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":980
     * # Versions of the import_* functions which are more suitable for
     * # Cython code.
     * cdef inline int import_array() except -1:             # <<<<<<<<<<<<<<
     *     try:
     *         __pyx_import_array()
     */

    /* function exit code */
    __pyx_r = 0;
    goto __pyx_L0;
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_5);
    __Pyx_XDECREF(__pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7);
    __Pyx_XDECREF(__pyx_t_8);
    __Pyx_AddTraceback("numpy.import_array", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = -1;
__pyx_L0:;
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":986
 *         raise ImportError("numpy.core.multiarray failed to import")
 *
 * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
 *     try:
 *         _import_umath()
 */

static CYTHON_INLINE int __pyx_f_5numpy_import_umath(void)
{
    int __pyx_r;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    int __pyx_t_4;
    PyObject *__pyx_t_5 = NULL;
    PyObject *__pyx_t_6 = NULL;
    PyObject *__pyx_t_7 = NULL;
    PyObject *__pyx_t_8 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("import_umath", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":987
     *
     * cdef inline int import_umath() except -1:
     *     try:             # <<<<<<<<<<<<<<
     *         _import_umath()
     *     except Exception:
     */
    {
        __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
                __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
        __Pyx_XGOTREF(__pyx_t_1);
        __Pyx_XGOTREF(__pyx_t_2);
        __Pyx_XGOTREF(__pyx_t_3);
        /*try:*/ {

            /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":988
             * cdef inline int import_umath() except -1:
             *     try:
             *         _import_umath()             # <<<<<<<<<<<<<<
             *     except Exception:
             *         raise ImportError("numpy.core.umath failed to import")
             */
            __pyx_t_4 = _import_umath();
            if (unlikely(__pyx_t_4 == ((int)-1)))
                __PYX_ERR(2, 988, __pyx_L3_error)

            /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":987
             *
             * cdef inline int import_umath() except -1:
             *     try:             # <<<<<<<<<<<<<<
             *         _import_umath()
             *     except Exception:
             */
        }
        __Pyx_XDECREF(__pyx_t_1);
        __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        goto __pyx_L8_try_end;
    __pyx_L3_error:;

        /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":989
         *     try:
         *         _import_umath()
         *     except Exception:             # <<<<<<<<<<<<<<
         *         raise ImportError("numpy.core.umath failed to import")
         *
         */
        __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject *)PyExc_Exception)[0])));
        if (__pyx_t_4)
        {
            __Pyx_AddTraceback("numpy.import_umath", __pyx_clineno, __pyx_lineno, __pyx_filename);
            if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0)
                __PYX_ERR(2, 989, __pyx_L5_except_error)
            __Pyx_XGOTREF(__pyx_t_5);
            __Pyx_XGOTREF(__pyx_t_6);
            __Pyx_XGOTREF(__pyx_t_7);

            /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":990
             *         _import_umath()
             *     except Exception:
             *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
             *
             * cdef inline int import_ufunc() except -1:
             */
            __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_ImportError, __pyx_tuple__2, NULL);
            if (unlikely(!__pyx_t_8))
                __PYX_ERR(2, 990, __pyx_L5_except_error)
            __Pyx_GOTREF(__pyx_t_8);
            __Pyx_Raise(__pyx_t_8, 0, 0, 0);
            __Pyx_DECREF(__pyx_t_8);
            __pyx_t_8 = 0;
            __PYX_ERR(2, 990, __pyx_L5_except_error)
        }
        goto __pyx_L5_except_error;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":987
     *
     * cdef inline int import_umath() except -1:
     *     try:             # <<<<<<<<<<<<<<
     *         _import_umath()
     *     except Exception:
     */
    __pyx_L5_except_error:;
        __Pyx_XGIVEREF(__pyx_t_1);
        __Pyx_XGIVEREF(__pyx_t_2);
        __Pyx_XGIVEREF(__pyx_t_3);
        __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
        goto __pyx_L1_error;
    __pyx_L8_try_end:;
    }

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":986
     *         raise ImportError("numpy.core.multiarray failed to import")
     *
     * cdef inline int import_umath() except -1:             # <<<<<<<<<<<<<<
     *     try:
     *         _import_umath()
     */

    /* function exit code */
    __pyx_r = 0;
    goto __pyx_L0;
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_5);
    __Pyx_XDECREF(__pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7);
    __Pyx_XDECREF(__pyx_t_8);
    __Pyx_AddTraceback("numpy.import_umath", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = -1;
__pyx_L0:;
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":992
 *         raise ImportError("numpy.core.umath failed to import")
 *
 * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
 *     try:
 *         _import_umath()
 */

static CYTHON_INLINE int __pyx_f_5numpy_import_ufunc(void)
{
    int __pyx_r;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    int __pyx_t_4;
    PyObject *__pyx_t_5 = NULL;
    PyObject *__pyx_t_6 = NULL;
    PyObject *__pyx_t_7 = NULL;
    PyObject *__pyx_t_8 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("import_ufunc", 1);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":993
     *
     * cdef inline int import_ufunc() except -1:
     *     try:             # <<<<<<<<<<<<<<
     *         _import_umath()
     *     except Exception:
     */
    {
        __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
                __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
        __Pyx_XGOTREF(__pyx_t_1);
        __Pyx_XGOTREF(__pyx_t_2);
        __Pyx_XGOTREF(__pyx_t_3);
        /*try:*/ {

            /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":994
             * cdef inline int import_ufunc() except -1:
             *     try:
             *         _import_umath()             # <<<<<<<<<<<<<<
             *     except Exception:
             *         raise ImportError("numpy.core.umath failed to import")
             */
            __pyx_t_4 = _import_umath();
            if (unlikely(__pyx_t_4 == ((int)-1)))
                __PYX_ERR(2, 994, __pyx_L3_error)

            /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":993
             *
             * cdef inline int import_ufunc() except -1:
             *     try:             # <<<<<<<<<<<<<<
             *         _import_umath()
             *     except Exception:
             */
        }
        __Pyx_XDECREF(__pyx_t_1);
        __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        goto __pyx_L8_try_end;
    __pyx_L3_error:;

        /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":995
         *     try:
         *         _import_umath()
         *     except Exception:             # <<<<<<<<<<<<<<
         *         raise ImportError("numpy.core.umath failed to import")
         *
         */
        __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject *)PyExc_Exception)[0])));
        if (__pyx_t_4)
        {
            __Pyx_AddTraceback("numpy.import_ufunc", __pyx_clineno, __pyx_lineno, __pyx_filename);
            if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7) < 0)
                __PYX_ERR(2, 995, __pyx_L5_except_error)
            __Pyx_XGOTREF(__pyx_t_5);
            __Pyx_XGOTREF(__pyx_t_6);
            __Pyx_XGOTREF(__pyx_t_7);

            /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":996
             *         _import_umath()
             *     except Exception:
             *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
             *
             *
             */
            __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_ImportError, __pyx_tuple__2, NULL);
            if (unlikely(!__pyx_t_8))
                __PYX_ERR(2, 996, __pyx_L5_except_error)
            __Pyx_GOTREF(__pyx_t_8);
            __Pyx_Raise(__pyx_t_8, 0, 0, 0);
            __Pyx_DECREF(__pyx_t_8);
            __pyx_t_8 = 0;
            __PYX_ERR(2, 996, __pyx_L5_except_error)
        }
        goto __pyx_L5_except_error;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":993
     *
     * cdef inline int import_ufunc() except -1:
     *     try:             # <<<<<<<<<<<<<<
     *         _import_umath()
     *     except Exception:
     */
    __pyx_L5_except_error:;
        __Pyx_XGIVEREF(__pyx_t_1);
        __Pyx_XGIVEREF(__pyx_t_2);
        __Pyx_XGIVEREF(__pyx_t_3);
        __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
        goto __pyx_L1_error;
    __pyx_L8_try_end:;
    }

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":992
     *         raise ImportError("numpy.core.umath failed to import")
     *
     * cdef inline int import_ufunc() except -1:             # <<<<<<<<<<<<<<
     *     try:
     *         _import_umath()
     */

    /* function exit code */
    __pyx_r = 0;
    goto __pyx_L0;
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_5);
    __Pyx_XDECREF(__pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7);
    __Pyx_XDECREF(__pyx_t_8);
    __Pyx_AddTraceback("numpy.import_ufunc", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = -1;
__pyx_L0:;
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":999
 *
 *
 * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
 *     """
 *     Cython equivalent of `isinstance(obj, np.timedelta64)`
 */

static CYTHON_INLINE int __pyx_f_5numpy_is_timedelta64_object(PyObject *__pyx_v_obj)
{
    int __pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1011
     *     bool
     *     """
     *     return PyObject_TypeCheck(obj, &PyTimedeltaArrType_Type)             # <<<<<<<<<<<<<<
     *
     *
     */
    __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyTimedeltaArrType_Type));
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":999
 *
 *
 * cdef inline bint is_timedelta64_object(object obj):             # <<<<<<<<<<<<<<
 *     """
 *     Cython equivalent of `isinstance(obj, np.timedelta64)`
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1014
 *
 *
 * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
 *     """
 *     Cython equivalent of `isinstance(obj, np.datetime64)`
 */

static CYTHON_INLINE int __pyx_f_5numpy_is_datetime64_object(PyObject *__pyx_v_obj)
{
    int __pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1026
     *     bool
     *     """
     *     return PyObject_TypeCheck(obj, &PyDatetimeArrType_Type)             # <<<<<<<<<<<<<<
     *
     *
     */
    __pyx_r = PyObject_TypeCheck(__pyx_v_obj, (&PyDatetimeArrType_Type));
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1014
 *
 *
 * cdef inline bint is_datetime64_object(object obj):             # <<<<<<<<<<<<<<
 *     """
 *     Cython equivalent of `isinstance(obj, np.datetime64)`
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1029
 *
 *
 * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
 *     """
 *     returns the int64 value underlying scalar numpy datetime64 object
 */

static CYTHON_INLINE npy_datetime __pyx_f_5numpy_get_datetime64_value(PyObject *__pyx_v_obj)
{
    npy_datetime __pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1036
     *     also needed.  That can be found using `get_datetime64_unit`.
     *     """
     *     return (<PyDatetimeScalarObject*>obj).obval             # <<<<<<<<<<<<<<
     *
     *
     */
    __pyx_r = ((PyDatetimeScalarObject *)__pyx_v_obj)->obval;
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1029
 *
 *
 * cdef inline npy_datetime get_datetime64_value(object obj) nogil:             # <<<<<<<<<<<<<<
 *     """
 *     returns the int64 value underlying scalar numpy datetime64 object
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1039
 *
 *
 * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
 *     """
 *     returns the int64 value underlying scalar numpy timedelta64 object
 */

static CYTHON_INLINE npy_timedelta __pyx_f_5numpy_get_timedelta64_value(PyObject *__pyx_v_obj)
{
    npy_timedelta __pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1043
     *     returns the int64 value underlying scalar numpy timedelta64 object
     *     """
     *     return (<PyTimedeltaScalarObject*>obj).obval             # <<<<<<<<<<<<<<
     *
     *
     */
    __pyx_r = ((PyTimedeltaScalarObject *)__pyx_v_obj)->obval;
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1039
 *
 *
 * cdef inline npy_timedelta get_timedelta64_value(object obj) nogil:             # <<<<<<<<<<<<<<
 *     """
 *     returns the int64 value underlying scalar numpy timedelta64 object
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1046
 *
 *
 * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
 *     """
 *     returns the unit part of the dtype for a numpy datetime64 object.
 */

static CYTHON_INLINE NPY_DATETIMEUNIT __pyx_f_5numpy_get_datetime64_unit(PyObject *__pyx_v_obj)
{
    NPY_DATETIMEUNIT __pyx_r;

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1050
     *     returns the unit part of the dtype for a numpy datetime64 object.
     *     """
     *     return <NPY_DATETIMEUNIT>(<PyDatetimeScalarObject*>obj).obmeta.base             # <<<<<<<<<<<<<<
     */
    __pyx_r = ((NPY_DATETIMEUNIT)((PyDatetimeScalarObject *)__pyx_v_obj)->obmeta.base);
    goto __pyx_L0;

/* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":1046
 *
 *
 * cdef inline NPY_DATETIMEUNIT get_datetime64_unit(object obj) nogil:             # <<<<<<<<<<<<<<
 *     """
 *     returns the unit part of the dtype for a numpy datetime64 object.
 */

/* function exit code */
__pyx_L0:;
    return __pyx_r;
}

/* "pyemd/emd.pyx":41
 *
 *
 * def _validate_emd_input(first_histogram, second_histogram, distance_matrix):             # <<<<<<<<<<<<<<
 *     """Validate EMD input."""
 *     if (first_histogram.shape[0] > distance_matrix.shape[0] or
 */

/* Python wrapper */
static PyObject *__pyx_pw_5pyemd_3emd_1_validate_emd_input(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                                           PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                                           PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_5pyemd_3emd__validate_emd_input, "Validate EMD input.");
static PyMethodDef __pyx_mdef_5pyemd_3emd_1_validate_emd_input = {"_validate_emd_input", (PyCFunction)(void *)(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_5pyemd_3emd_1_validate_emd_input, __Pyx_METH_FASTCALL | METH_KEYWORDS, __pyx_doc_5pyemd_3emd__validate_emd_input};
static PyObject *__pyx_pw_5pyemd_3emd_1_validate_emd_input(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                                           PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                                           PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
)
{
    PyObject *__pyx_v_first_histogram = 0;
    PyObject *__pyx_v_second_histogram = 0;
    PyObject *__pyx_v_distance_matrix = 0;
#if !CYTHON_METH_FASTCALL
    CYTHON_UNUSED Py_ssize_t __pyx_nargs;
#endif
    CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
    PyObject *values[3] = {0, 0, 0};
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    PyObject *__pyx_r = 0;
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("_validate_emd_input (wrapper)", 0);
#if !CYTHON_METH_FASTCALL
#if CYTHON_ASSUME_SAFE_MACROS
    __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
#else
    __pyx_nargs = PyTuple_Size(__pyx_args);
    if (unlikely(__pyx_nargs < 0))
        return NULL;
#endif
#endif
    __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
    {
        PyObject **__pyx_pyargnames[] = {&__pyx_n_s_first_histogram, &__pyx_n_s_second_histogram, &__pyx_n_s_distance_matrix, 0};
        if (__pyx_kwds)
        {
            Py_ssize_t kw_args;
            switch (__pyx_nargs)
            {
            case 3:
                values[2] = __Pyx_Arg_FASTCALL(__pyx_args, 2);
                CYTHON_FALLTHROUGH;
            case 2:
                values[1] = __Pyx_Arg_FASTCALL(__pyx_args, 1);
                CYTHON_FALLTHROUGH;
            case 1:
                values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
                CYTHON_FALLTHROUGH;
            case 0:
                break;
            default:
                goto __pyx_L5_argtuple_error;
            }
            kw_args = __Pyx_NumKwargs_FASTCALL(__pyx_kwds);
            switch (__pyx_nargs)
            {
            case 0:
                if (likely((values[0] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_first_histogram)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[0]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 41, __pyx_L3_error)
                else
                    goto __pyx_L5_argtuple_error;
                CYTHON_FALLTHROUGH;
            case 1:
                if (likely((values[1] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_second_histogram)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[1]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 41, __pyx_L3_error)
                else
                {
                    __Pyx_RaiseArgtupleInvalid("_validate_emd_input", 1, 3, 3, 1);
                    __PYX_ERR(0, 41, __pyx_L3_error)
                }
                CYTHON_FALLTHROUGH;
            case 2:
                if (likely((values[2] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_distance_matrix)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[2]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 41, __pyx_L3_error)
                else
                {
                    __Pyx_RaiseArgtupleInvalid("_validate_emd_input", 1, 3, 3, 2);
                    __PYX_ERR(0, 41, __pyx_L3_error)
                }
            }
            if (unlikely(kw_args > 0))
            {
                const Py_ssize_t kwd_pos_args = __pyx_nargs;
                if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values + 0, kwd_pos_args, "_validate_emd_input") < 0))
                    __PYX_ERR(0, 41, __pyx_L3_error)
            }
        }
        else if (unlikely(__pyx_nargs != 3))
        {
            goto __pyx_L5_argtuple_error;
        }
        else
        {
            values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
            values[1] = __Pyx_Arg_FASTCALL(__pyx_args, 1);
            values[2] = __Pyx_Arg_FASTCALL(__pyx_args, 2);
        }
        __pyx_v_first_histogram = values[0];
        __pyx_v_second_histogram = values[1];
        __pyx_v_distance_matrix = values[2];
    }
    goto __pyx_L6_skip;
__pyx_L5_argtuple_error:;
    __Pyx_RaiseArgtupleInvalid("_validate_emd_input", 1, 3, 3, __pyx_nargs);
    __PYX_ERR(0, 41, __pyx_L3_error)
__pyx_L6_skip:;
    goto __pyx_L4_argument_unpacking_done;
__pyx_L3_error:;
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_AddTraceback("pyemd.emd._validate_emd_input", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __Pyx_RefNannyFinishContext();
    return NULL;
__pyx_L4_argument_unpacking_done:;
    __pyx_r = __pyx_pf_5pyemd_3emd__validate_emd_input(__pyx_self, __pyx_v_first_histogram, __pyx_v_second_histogram, __pyx_v_distance_matrix);

    /* function exit code */
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

static PyObject *__pyx_pf_5pyemd_3emd__validate_emd_input(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_first_histogram, PyObject *__pyx_v_second_histogram, PyObject *__pyx_v_distance_matrix)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations int __pyx_t_1;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    PyObject *__pyx_t_4 = NULL;
    int __pyx_t_5;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("_validate_emd_input", 1);

    /* "pyemd/emd.pyx":43
     * def _validate_emd_input(first_histogram, second_histogram, distance_matrix):
     *     """Validate EMD input."""
     *     if (first_histogram.shape[0] > distance_matrix.shape[0] or             # <<<<<<<<<<<<<<
     *         second_histogram.shape[0] > distance_matrix.shape[0]):
     *         raise ValueError('Histogram lengths cannot be greater than the '
     */
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_first_histogram, __pyx_n_s_shape);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 43, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_GetItemInt(__pyx_t_2, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1);
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 43, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_distance_matrix, __pyx_n_s_shape);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 43, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_2, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1);
    if (unlikely(!__pyx_t_4))
        __PYX_ERR(0, 43, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_2 = PyObject_RichCompare(__pyx_t_3, __pyx_t_4, Py_GT);
    __Pyx_XGOTREF(__pyx_t_2);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 43, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_2);
    if (unlikely((__pyx_t_5 < 0)))
        __PYX_ERR(0, 43, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    if (!__pyx_t_5)
    {
    }
    else
    {
        __pyx_t_1 = __pyx_t_5;
        goto __pyx_L4_bool_binop_done;
    }

    /* "pyemd/emd.pyx":44
     *     """Validate EMD input."""
     *     if (first_histogram.shape[0] > distance_matrix.shape[0] or
     *         second_histogram.shape[0] > distance_matrix.shape[0]):             # <<<<<<<<<<<<<<
     *         raise ValueError('Histogram lengths cannot be greater than the '
     *                          'number of rows or columns of the distance matrix')
     */
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_second_histogram, __pyx_n_s_shape);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 44, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_2, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1);
    if (unlikely(!__pyx_t_4))
        __PYX_ERR(0, 44, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_distance_matrix, __pyx_n_s_shape);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 44, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_GetItemInt(__pyx_t_2, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1);
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 44, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_2 = PyObject_RichCompare(__pyx_t_4, __pyx_t_3, Py_GT);
    __Pyx_XGOTREF(__pyx_t_2);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 44, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_2);
    if (unlikely((__pyx_t_5 < 0)))
        __PYX_ERR(0, 44, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_1 = __pyx_t_5;
__pyx_L4_bool_binop_done:;

    /* "pyemd/emd.pyx":43
     * def _validate_emd_input(first_histogram, second_histogram, distance_matrix):
     *     """Validate EMD input."""
     *     if (first_histogram.shape[0] > distance_matrix.shape[0] or             # <<<<<<<<<<<<<<
     *         second_histogram.shape[0] > distance_matrix.shape[0]):
     *         raise ValueError('Histogram lengths cannot be greater than the '
     */
    if (unlikely(__pyx_t_1))
    {

        /* "pyemd/emd.pyx":45
         *     if (first_histogram.shape[0] > distance_matrix.shape[0] or
         *         second_histogram.shape[0] > distance_matrix.shape[0]):
         *         raise ValueError('Histogram lengths cannot be greater than the '             # <<<<<<<<<<<<<<
         *                          'number of rows or columns of the distance matrix')
         *     if (first_histogram.shape[0] != second_histogram.shape[0]):
         */
        __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_ValueError, __pyx_tuple__3, NULL);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 45, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_Raise(__pyx_t_2, 0, 0, 0);
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __PYX_ERR(0, 45, __pyx_L1_error)

        /* "pyemd/emd.pyx":43
         * def _validate_emd_input(first_histogram, second_histogram, distance_matrix):
         *     """Validate EMD input."""
         *     if (first_histogram.shape[0] > distance_matrix.shape[0] or             # <<<<<<<<<<<<<<
         *         second_histogram.shape[0] > distance_matrix.shape[0]):
         *         raise ValueError('Histogram lengths cannot be greater than the '
         */
    }

    /* "pyemd/emd.pyx":47
     *         raise ValueError('Histogram lengths cannot be greater than the '
     *                          'number of rows or columns of the distance matrix')
     *     if (first_histogram.shape[0] != second_histogram.shape[0]):             # <<<<<<<<<<<<<<
     *         raise ValueError('Histogram lengths must be equal')
     *
     */
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_first_histogram, __pyx_n_s_shape);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 47, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_GetItemInt(__pyx_t_2, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1);
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 47, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_second_histogram, __pyx_n_s_shape);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 47, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_2, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1);
    if (unlikely(!__pyx_t_4))
        __PYX_ERR(0, 47, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_2 = PyObject_RichCompare(__pyx_t_3, __pyx_t_4, Py_NE);
    __Pyx_XGOTREF(__pyx_t_2);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 47, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_1 = __Pyx_PyObject_IsTrue(__pyx_t_2);
    if (unlikely((__pyx_t_1 < 0)))
        __PYX_ERR(0, 47, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    if (unlikely(__pyx_t_1))
    {

        /* "pyemd/emd.pyx":48
         *                          'number of rows or columns of the distance matrix')
         *     if (first_histogram.shape[0] != second_histogram.shape[0]):
         *         raise ValueError('Histogram lengths must be equal')             # <<<<<<<<<<<<<<
         *
         *
         */
        __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_ValueError, __pyx_tuple__4, NULL);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 48, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_Raise(__pyx_t_2, 0, 0, 0);
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __PYX_ERR(0, 48, __pyx_L1_error)

        /* "pyemd/emd.pyx":47
         *         raise ValueError('Histogram lengths cannot be greater than the '
         *                          'number of rows or columns of the distance matrix')
         *     if (first_histogram.shape[0] != second_histogram.shape[0]):             # <<<<<<<<<<<<<<
         *         raise ValueError('Histogram lengths must be equal')
         *
         */
    }

    /* "pyemd/emd.pyx":41
     *
     *
     * def _validate_emd_input(first_histogram, second_histogram, distance_matrix):             # <<<<<<<<<<<<<<
     *     """Validate EMD input."""
     *     if (first_histogram.shape[0] > distance_matrix.shape[0] or
     */

    /* function exit code */
    __pyx_r = Py_None;
    __Pyx_INCREF(Py_None);
    goto __pyx_L0;
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_3);
    __Pyx_XDECREF(__pyx_t_4);
    __Pyx_AddTraceback("pyemd.emd._validate_emd_input", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = NULL;
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "pyemd/emd.pyx":51
 *
 *
 * def emd(np.ndarray[np.float64_t, ndim=1, mode="c"] first_histogram,             # <<<<<<<<<<<<<<
 *         np.ndarray[np.float64_t, ndim=1, mode="c"] second_histogram,
 *         np.ndarray[np.float64_t, ndim=2, mode="c"] distance_matrix,
 */

static PyObject *__pyx_pf_5pyemd_3emd_12__defaults__(CYTHON_UNUSED PyObject *__pyx_self)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("__defaults__", 1);
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_1 = PyTuple_New(1);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 51, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_INCREF(__Pyx_CyFunction_Defaults(__pyx_defaults, __pyx_self)->__pyx_arg_extra_mass_penalty);
    __Pyx_GIVEREF(__Pyx_CyFunction_Defaults(__pyx_defaults, __pyx_self)->__pyx_arg_extra_mass_penalty);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __Pyx_CyFunction_Defaults(__pyx_defaults, __pyx_self)->__pyx_arg_extra_mass_penalty))
        __PYX_ERR(0, 51, __pyx_L1_error);
    __pyx_t_2 = PyTuple_New(2);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 51, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_GIVEREF(__pyx_t_1);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_1))
        __PYX_ERR(0, 51, __pyx_L1_error);
    __Pyx_INCREF(Py_None);
    __Pyx_GIVEREF(Py_None);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_2, 1, Py_None))
        __PYX_ERR(0, 51, __pyx_L1_error);
    __pyx_t_1 = 0;
    __pyx_r = __pyx_t_2;
    __pyx_t_2 = 0;
    goto __pyx_L0;

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_AddTraceback("pyemd.emd.__defaults__", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = NULL;
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* Python wrapper */
static PyObject *__pyx_pw_5pyemd_3emd_3emd(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                           PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                           PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_5pyemd_3emd_2emd, "Return the EMD between two histograms using the given distance matrix.\n\n    The Earth Mover's Distance is the minimal cost of turning one histogram into\n    another by moving around the \342\200\234dirt\342\200\235 in the bins, where the cost of moving\n    dirt from one bin to another is given by the amount of dirt times the\n    \342\200\234ground distance\342\200\235 between the bins.\n\n    Arguments:\n        first_histogram (np.ndarray): A 1D array of type np.float64 of length N.\n        second_histogram (np.ndarray): A 1D array of np.float64 of length N.\n        distance_matrix (np.ndarray): A 2D array of np.float64, of size at least\n            N \303\227 N. This defines the underlying metric, or ground distance, by\n            giving the pairwise distances between the histogram bins. It must\n            represent a metric; there is no warning if it doesn't.\n\n    Keyword Arguments:\n        extra_mass_penalty (float): The penalty for extra mass. If you want the\n            resulting distance to be a metric, it should be at least half the\n            diameter of the space (maximum possible distance between any two\n            points). If you want partial matching you can set it to zero (but\n            then the resulting distance is not guaranteed to be a metric). The\n            default value is -1, which means the maximum value in the distance\n            matrix is used.\n\n    Returns:\n        float: The EMD value.\n\n    Raises:\n        ValueError: If the length of either histogram is greater than the number\n        of rows or columns of the distance matrix, or if the histograms aren't\n        the same length.\n    ");
static PyMethodDef __pyx_mdef_5pyemd_3emd_3emd = {"emd", (PyCFunction)(void *)(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_5pyemd_3emd_3emd, __Pyx_METH_FASTCALL | METH_KEYWORDS, __pyx_doc_5pyemd_3emd_2emd};
static PyObject *__pyx_pw_5pyemd_3emd_3emd(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                           PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                           PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
)
{
    PyArrayObject *__pyx_v_first_histogram = 0;
    PyArrayObject *__pyx_v_second_histogram = 0;
    PyArrayObject *__pyx_v_distance_matrix = 0;
    PyObject *__pyx_v_extra_mass_penalty = 0;
#if !CYTHON_METH_FASTCALL
    CYTHON_UNUSED Py_ssize_t __pyx_nargs;
#endif
    CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
    PyObject *values[4] = {0, 0, 0, 0};
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    PyObject *__pyx_r = 0;
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("emd (wrapper)", 0);
#if !CYTHON_METH_FASTCALL
#if CYTHON_ASSUME_SAFE_MACROS
    __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
#else
    __pyx_nargs = PyTuple_Size(__pyx_args);
    if (unlikely(__pyx_nargs < 0))
        return NULL;
#endif
#endif
    __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
    {
        PyObject **__pyx_pyargnames[] = {&__pyx_n_s_first_histogram, &__pyx_n_s_second_histogram, &__pyx_n_s_distance_matrix, &__pyx_n_s_extra_mass_penalty, 0};
        __pyx_defaults *__pyx_dynamic_args = __Pyx_CyFunction_Defaults(__pyx_defaults, __pyx_self);
        values[3] = __Pyx_Arg_NewRef_FASTCALL(__pyx_dynamic_args->__pyx_arg_extra_mass_penalty);
        if (__pyx_kwds)
        {
            Py_ssize_t kw_args;
            switch (__pyx_nargs)
            {
            case 4:
                values[3] = __Pyx_Arg_FASTCALL(__pyx_args, 3);
                CYTHON_FALLTHROUGH;
            case 3:
                values[2] = __Pyx_Arg_FASTCALL(__pyx_args, 2);
                CYTHON_FALLTHROUGH;
            case 2:
                values[1] = __Pyx_Arg_FASTCALL(__pyx_args, 1);
                CYTHON_FALLTHROUGH;
            case 1:
                values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
                CYTHON_FALLTHROUGH;
            case 0:
                break;
            default:
                goto __pyx_L5_argtuple_error;
            }
            kw_args = __Pyx_NumKwargs_FASTCALL(__pyx_kwds);
            switch (__pyx_nargs)
            {
            case 0:
                if (likely((values[0] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_first_histogram)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[0]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 51, __pyx_L3_error)
                else
                    goto __pyx_L5_argtuple_error;
                CYTHON_FALLTHROUGH;
            case 1:
                if (likely((values[1] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_second_histogram)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[1]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 51, __pyx_L3_error)
                else
                {
                    __Pyx_RaiseArgtupleInvalid("emd", 0, 3, 4, 1);
                    __PYX_ERR(0, 51, __pyx_L3_error)
                }
                CYTHON_FALLTHROUGH;
            case 2:
                if (likely((values[2] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_distance_matrix)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[2]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 51, __pyx_L3_error)
                else
                {
                    __Pyx_RaiseArgtupleInvalid("emd", 0, 3, 4, 2);
                    __PYX_ERR(0, 51, __pyx_L3_error)
                }
                CYTHON_FALLTHROUGH;
            case 3:
                if (kw_args > 0)
                {
                    PyObject *value = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_extra_mass_penalty);
                    if (value)
                    {
                        values[3] = __Pyx_Arg_NewRef_FASTCALL(value);
                        kw_args--;
                    }
                    else if (unlikely(PyErr_Occurred()))
                        __PYX_ERR(0, 51, __pyx_L3_error)
                }
            }
            if (unlikely(kw_args > 0))
            {
                const Py_ssize_t kwd_pos_args = __pyx_nargs;
                if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values + 0, kwd_pos_args, "emd") < 0))
                    __PYX_ERR(0, 51, __pyx_L3_error)
            }
        }
        else
        {
            switch (__pyx_nargs)
            {
            case 4:
                values[3] = __Pyx_Arg_FASTCALL(__pyx_args, 3);
                CYTHON_FALLTHROUGH;
            case 3:
                values[2] = __Pyx_Arg_FASTCALL(__pyx_args, 2);
                values[1] = __Pyx_Arg_FASTCALL(__pyx_args, 1);
                values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
                break;
            default:
                goto __pyx_L5_argtuple_error;
            }
        }
        __pyx_v_first_histogram = ((PyArrayObject *)values[0]);
        __pyx_v_second_histogram = ((PyArrayObject *)values[1]);
        __pyx_v_distance_matrix = ((PyArrayObject *)values[2]);
        __pyx_v_extra_mass_penalty = values[3];
    }
    goto __pyx_L6_skip;
__pyx_L5_argtuple_error:;
    __Pyx_RaiseArgtupleInvalid("emd", 0, 3, 4, __pyx_nargs);
    __PYX_ERR(0, 51, __pyx_L3_error)
__pyx_L6_skip:;
    goto __pyx_L4_argument_unpacking_done;
__pyx_L3_error:;
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_AddTraceback("pyemd.emd.emd", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __Pyx_RefNannyFinishContext();
    return NULL;
__pyx_L4_argument_unpacking_done:;
    if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_first_histogram), __pyx_ptype_5numpy_ndarray, 1, "first_histogram", 0)))
        __PYX_ERR(0, 51, __pyx_L1_error)
    if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_second_histogram), __pyx_ptype_5numpy_ndarray, 1, "second_histogram", 0)))
        __PYX_ERR(0, 52, __pyx_L1_error)
    if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_distance_matrix), __pyx_ptype_5numpy_ndarray, 1, "distance_matrix", 0)))
        __PYX_ERR(0, 53, __pyx_L1_error)
    __pyx_r = __pyx_pf_5pyemd_3emd_2emd(__pyx_self, __pyx_v_first_histogram, __pyx_v_second_histogram, __pyx_v_distance_matrix, __pyx_v_extra_mass_penalty);

    /* function exit code */
    goto __pyx_L0;
__pyx_L1_error:;
    __pyx_r = NULL;
__pyx_L0:;
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

static PyObject *__pyx_pf_5pyemd_3emd_2emd(CYTHON_UNUSED PyObject *__pyx_self, PyArrayObject *__pyx_v_first_histogram, PyArrayObject *__pyx_v_second_histogram, PyArrayObject *__pyx_v_distance_matrix, PyObject *__pyx_v_extra_mass_penalty)
{
    __Pyx_LocalBuf_ND __pyx_pybuffernd_distance_matrix;
    __Pyx_Buffer __pyx_pybuffer_distance_matrix;
    __Pyx_LocalBuf_ND __pyx_pybuffernd_first_histogram;
    __Pyx_Buffer __pyx_pybuffer_first_histogram;
    __Pyx_LocalBuf_ND __pyx_pybuffernd_second_histogram;
    __Pyx_Buffer __pyx_pybuffer_second_histogram;
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    int __pyx_t_4;
    std::vector<double> __pyx_t_5;
    std::vector<double> __pyx_t_6;
    std::vector<std::vector<double>> __pyx_t_7;
    double __pyx_t_8;
    double __pyx_t_9;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("emd", 1);
    __pyx_pybuffer_first_histogram.pybuffer.buf = NULL;
    __pyx_pybuffer_first_histogram.refcount = 0;
    __pyx_pybuffernd_first_histogram.data = NULL;
    __pyx_pybuffernd_first_histogram.rcbuffer = &__pyx_pybuffer_first_histogram;
    __pyx_pybuffer_second_histogram.pybuffer.buf = NULL;
    __pyx_pybuffer_second_histogram.refcount = 0;
    __pyx_pybuffernd_second_histogram.data = NULL;
    __pyx_pybuffernd_second_histogram.rcbuffer = &__pyx_pybuffer_second_histogram;
    __pyx_pybuffer_distance_matrix.pybuffer.buf = NULL;
    __pyx_pybuffer_distance_matrix.refcount = 0;
    __pyx_pybuffernd_distance_matrix.data = NULL;
    __pyx_pybuffernd_distance_matrix.rcbuffer = &__pyx_pybuffer_distance_matrix;
    {
        __Pyx_BufFmt_StackElem __pyx_stack[1];
        if (unlikely(__Pyx_GetBufferAndValidate(&__pyx_pybuffernd_first_histogram.rcbuffer->pybuffer, (PyObject *)__pyx_v_first_histogram, &__Pyx_TypeInfo_nn___pyx_t_5numpy_float64_t, PyBUF_FORMAT | PyBUF_C_CONTIGUOUS, 1, 0, __pyx_stack) == -1))
            __PYX_ERR(0, 51, __pyx_L1_error)
    }
    __pyx_pybuffernd_first_histogram.diminfo[0].strides = __pyx_pybuffernd_first_histogram.rcbuffer->pybuffer.strides[0];
    __pyx_pybuffernd_first_histogram.diminfo[0].shape = __pyx_pybuffernd_first_histogram.rcbuffer->pybuffer.shape[0];
    {
        __Pyx_BufFmt_StackElem __pyx_stack[1];
        if (unlikely(__Pyx_GetBufferAndValidate(&__pyx_pybuffernd_second_histogram.rcbuffer->pybuffer, (PyObject *)__pyx_v_second_histogram, &__Pyx_TypeInfo_nn___pyx_t_5numpy_float64_t, PyBUF_FORMAT | PyBUF_C_CONTIGUOUS, 1, 0, __pyx_stack) == -1))
            __PYX_ERR(0, 51, __pyx_L1_error)
    }
    __pyx_pybuffernd_second_histogram.diminfo[0].strides = __pyx_pybuffernd_second_histogram.rcbuffer->pybuffer.strides[0];
    __pyx_pybuffernd_second_histogram.diminfo[0].shape = __pyx_pybuffernd_second_histogram.rcbuffer->pybuffer.shape[0];
    {
        __Pyx_BufFmt_StackElem __pyx_stack[1];
        if (unlikely(__Pyx_GetBufferAndValidate(&__pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer, (PyObject *)__pyx_v_distance_matrix, &__Pyx_TypeInfo_nn___pyx_t_5numpy_float64_t, PyBUF_FORMAT | PyBUF_C_CONTIGUOUS, 2, 0, __pyx_stack) == -1))
            __PYX_ERR(0, 51, __pyx_L1_error)
    }
    __pyx_pybuffernd_distance_matrix.diminfo[0].strides = __pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer.strides[0];
    __pyx_pybuffernd_distance_matrix.diminfo[0].shape = __pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer.shape[0];
    __pyx_pybuffernd_distance_matrix.diminfo[1].strides = __pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer.strides[1];
    __pyx_pybuffernd_distance_matrix.diminfo[1].shape = __pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer.shape[1];

    /* "pyemd/emd.pyx":87
     *         the same length.
     *     """
     *     _validate_emd_input(first_histogram, second_histogram, distance_matrix)             # <<<<<<<<<<<<<<
     *     return emd_hat_gd_metric_double(first_histogram,
     *                                     second_histogram,
     */
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_validate_emd_input);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 87, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = NULL;
    __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_2)))
    {
        __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
        if (likely(__pyx_t_3))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
            __pyx_t_4 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[4] = {__pyx_t_3, ((PyObject *)__pyx_v_first_histogram), ((PyObject *)__pyx_v_second_histogram), ((PyObject *)__pyx_v_distance_matrix)};
        __pyx_t_1 = __Pyx_PyObject_FastCall(__pyx_t_2, __pyx_callargs + 1 - __pyx_t_4, 3 + __pyx_t_4);
        __Pyx_XDECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 87, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
    }
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;

    /* "pyemd/emd.pyx":88
     *     """
     *     _validate_emd_input(first_histogram, second_histogram, distance_matrix)
     *     return emd_hat_gd_metric_double(first_histogram,             # <<<<<<<<<<<<<<
     *                                     second_histogram,
     *                                     distance_matrix,
     */
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_5 = __pyx_convert_vector_from_py_double(((PyObject *)__pyx_v_first_histogram));
    if (unlikely(PyErr_Occurred()))
        __PYX_ERR(0, 88, __pyx_L1_error)

    /* "pyemd/emd.pyx":89
     *     _validate_emd_input(first_histogram, second_histogram, distance_matrix)
     *     return emd_hat_gd_metric_double(first_histogram,
     *                                     second_histogram,             # <<<<<<<<<<<<<<
     *                                     distance_matrix,
     *                                     extra_mass_penalty)
     */
    __pyx_t_6 = __pyx_convert_vector_from_py_double(((PyObject *)__pyx_v_second_histogram));
    if (unlikely(PyErr_Occurred()))
        __PYX_ERR(0, 89, __pyx_L1_error)

    /* "pyemd/emd.pyx":90
     *     return emd_hat_gd_metric_double(first_histogram,
     *                                     second_histogram,
     *                                     distance_matrix,             # <<<<<<<<<<<<<<
     *                                     extra_mass_penalty)
     *
     */
    __pyx_t_7 = __pyx_convert_vector_from_py_std_3a__3a_vector_3c_double_3e___(((PyObject *)__pyx_v_distance_matrix));
    if (unlikely(PyErr_Occurred()))
        __PYX_ERR(0, 90, __pyx_L1_error)

    /* "pyemd/emd.pyx":91
     *                                     second_histogram,
     *                                     distance_matrix,
     *                                     extra_mass_penalty)             # <<<<<<<<<<<<<<
     *
     *
     */
    __pyx_t_8 = __pyx_PyFloat_AsDouble(__pyx_v_extra_mass_penalty);
    if (unlikely((__pyx_t_8 == (double)-1) && PyErr_Occurred()))
        __PYX_ERR(0, 91, __pyx_L1_error)

    /* "pyemd/emd.pyx":88
     *     """
     *     _validate_emd_input(first_histogram, second_histogram, distance_matrix)
     *     return emd_hat_gd_metric_double(first_histogram,             # <<<<<<<<<<<<<<
     *                                     second_histogram,
     *                                     distance_matrix,
     */
    try
    {
        __pyx_t_9 = emd_hat_gd_metric_double(__PYX_STD_MOVE_IF_SUPPORTED(__pyx_t_5), __PYX_STD_MOVE_IF_SUPPORTED(__pyx_t_6), __PYX_STD_MOVE_IF_SUPPORTED(__pyx_t_7), __pyx_t_8);
    }
    catch (...)
    {
        __Pyx_CppExn2PyErr();
        __PYX_ERR(0, 88, __pyx_L1_error)
    }
    __pyx_t_1 = PyFloat_FromDouble(__pyx_t_9);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 88, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_r = __pyx_t_1;
    __pyx_t_1 = 0;
    goto __pyx_L0;

/* "pyemd/emd.pyx":51
 *
 *
 * def emd(np.ndarray[np.float64_t, ndim=1, mode="c"] first_histogram,             # <<<<<<<<<<<<<<
 *         np.ndarray[np.float64_t, ndim=1, mode="c"] second_histogram,
 *         np.ndarray[np.float64_t, ndim=2, mode="c"] distance_matrix,
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_3);
    {
        PyObject *__pyx_type, *__pyx_value, *__pyx_tb;
        __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
                __Pyx_ErrFetch(&__pyx_type, &__pyx_value, &__pyx_tb);
        __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer);
        __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_first_histogram.rcbuffer->pybuffer);
        __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_second_histogram.rcbuffer->pybuffer);
        __Pyx_ErrRestore(__pyx_type, __pyx_value, __pyx_tb);
    }
    __Pyx_AddTraceback("pyemd.emd.emd", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = NULL;
    goto __pyx_L2;
__pyx_L0:;
    __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer);
    __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_first_histogram.rcbuffer->pybuffer);
    __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_second_histogram.rcbuffer->pybuffer);
__pyx_L2:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "pyemd/emd.pyx":94
 *
 *
 * def emd_with_flow(np.ndarray[np.float64_t, ndim=1, mode="c"] first_histogram,             # <<<<<<<<<<<<<<
 *                   np.ndarray[np.float64_t, ndim=1, mode="c"] second_histogram,
 *                   np.ndarray[np.float64_t, ndim=2, mode="c"] distance_matrix,
 */

static PyObject *__pyx_pf_5pyemd_3emd_14__defaults__(CYTHON_UNUSED PyObject *__pyx_self)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("__defaults__", 1);
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_1 = PyTuple_New(1);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 94, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_INCREF(__Pyx_CyFunction_Defaults(__pyx_defaults1, __pyx_self)->__pyx_arg_extra_mass_penalty);
    __Pyx_GIVEREF(__Pyx_CyFunction_Defaults(__pyx_defaults1, __pyx_self)->__pyx_arg_extra_mass_penalty);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __Pyx_CyFunction_Defaults(__pyx_defaults1, __pyx_self)->__pyx_arg_extra_mass_penalty))
        __PYX_ERR(0, 94, __pyx_L1_error);
    __pyx_t_2 = PyTuple_New(2);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 94, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_GIVEREF(__pyx_t_1);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_1))
        __PYX_ERR(0, 94, __pyx_L1_error);
    __Pyx_INCREF(Py_None);
    __Pyx_GIVEREF(Py_None);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_2, 1, Py_None))
        __PYX_ERR(0, 94, __pyx_L1_error);
    __pyx_t_1 = 0;
    __pyx_r = __pyx_t_2;
    __pyx_t_2 = 0;
    goto __pyx_L0;

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_AddTraceback("pyemd.emd.__defaults__", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = NULL;
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* Python wrapper */
static PyObject *__pyx_pw_5pyemd_3emd_5emd_with_flow(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                                     PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                                     PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_5pyemd_3emd_4emd_with_flow, "Return the EMD between two histograms using the given distance matrix.\n\n    The Earth Mover's Distance is the minimal cost of turning one histogram into\n    another by moving around the \342\200\234dirt\342\200\235 in the bins, where the cost of the\n    \342\200\234ground distance\342\200\235 between the bins. moving dirt from one bin to another is\n    given by the amount of dirt times\n\n    Arguments:\n        first_histogram (np.ndarray): A 1D array of type np.float64 of length N.\n        second_histogram (np.ndarray): A 1D array of np.float64 of length N.\n        distance_matrix (np.ndarray): A 2D array of np.float64, of size at least\n            N \303\227 N. This defines the underlying metric, or ground distance, by\n            giving the pairwise distances between the histogram bins. It must\n            represent a metric; there is no warning if it doesn't.\n\n    Keyword Arguments:\n        extra_mass_penalty (float): The penalty for extra mass. If you want the\n            resulting distance to be a metric, it should be at least half the\n            diameter of the space (maximum possible distance between any two\n            points). If you want partial matching you can set it to zero (but\n            then the resulting distance is not guaranteed to be a metric). The\n            default value is -1, which means the maximum value in the distance\n            matrix is used.\n\n    Returns:\n        (tuple(float, list(list(float)))): The EMD value and the associated\n        minimum-cost flow.\n\n    Raises:\n        ValueError: If the length of either histogram is greater than the number\n        of rows or columns of the distance matrix, or if the histograms aren't\n        the same length.\n    ");
static PyMethodDef __pyx_mdef_5pyemd_3emd_5emd_with_flow = {"emd_with_flow", (PyCFunction)(void *)(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_5pyemd_3emd_5emd_with_flow, __Pyx_METH_FASTCALL | METH_KEYWORDS, __pyx_doc_5pyemd_3emd_4emd_with_flow};
static PyObject *__pyx_pw_5pyemd_3emd_5emd_with_flow(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                                     PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                                     PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
)
{
    PyArrayObject *__pyx_v_first_histogram = 0;
    PyArrayObject *__pyx_v_second_histogram = 0;
    PyArrayObject *__pyx_v_distance_matrix = 0;
    PyObject *__pyx_v_extra_mass_penalty = 0;
#if !CYTHON_METH_FASTCALL
    CYTHON_UNUSED Py_ssize_t __pyx_nargs;
#endif
    CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
    PyObject *values[4] = {0, 0, 0, 0};
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    PyObject *__pyx_r = 0;
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("emd_with_flow (wrapper)", 0);
#if !CYTHON_METH_FASTCALL
#if CYTHON_ASSUME_SAFE_MACROS
    __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
#else
    __pyx_nargs = PyTuple_Size(__pyx_args);
    if (unlikely(__pyx_nargs < 0))
        return NULL;
#endif
#endif
    __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
    {
        PyObject **__pyx_pyargnames[] = {&__pyx_n_s_first_histogram, &__pyx_n_s_second_histogram, &__pyx_n_s_distance_matrix, &__pyx_n_s_extra_mass_penalty, 0};
        __pyx_defaults1 *__pyx_dynamic_args = __Pyx_CyFunction_Defaults(__pyx_defaults1, __pyx_self);
        values[3] = __Pyx_Arg_NewRef_FASTCALL(__pyx_dynamic_args->__pyx_arg_extra_mass_penalty);
        if (__pyx_kwds)
        {
            Py_ssize_t kw_args;
            switch (__pyx_nargs)
            {
            case 4:
                values[3] = __Pyx_Arg_FASTCALL(__pyx_args, 3);
                CYTHON_FALLTHROUGH;
            case 3:
                values[2] = __Pyx_Arg_FASTCALL(__pyx_args, 2);
                CYTHON_FALLTHROUGH;
            case 2:
                values[1] = __Pyx_Arg_FASTCALL(__pyx_args, 1);
                CYTHON_FALLTHROUGH;
            case 1:
                values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
                CYTHON_FALLTHROUGH;
            case 0:
                break;
            default:
                goto __pyx_L5_argtuple_error;
            }
            kw_args = __Pyx_NumKwargs_FASTCALL(__pyx_kwds);
            switch (__pyx_nargs)
            {
            case 0:
                if (likely((values[0] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_first_histogram)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[0]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 94, __pyx_L3_error)
                else
                    goto __pyx_L5_argtuple_error;
                CYTHON_FALLTHROUGH;
            case 1:
                if (likely((values[1] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_second_histogram)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[1]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 94, __pyx_L3_error)
                else
                {
                    __Pyx_RaiseArgtupleInvalid("emd_with_flow", 0, 3, 4, 1);
                    __PYX_ERR(0, 94, __pyx_L3_error)
                }
                CYTHON_FALLTHROUGH;
            case 2:
                if (likely((values[2] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_distance_matrix)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[2]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 94, __pyx_L3_error)
                else
                {
                    __Pyx_RaiseArgtupleInvalid("emd_with_flow", 0, 3, 4, 2);
                    __PYX_ERR(0, 94, __pyx_L3_error)
                }
                CYTHON_FALLTHROUGH;
            case 3:
                if (kw_args > 0)
                {
                    PyObject *value = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_extra_mass_penalty);
                    if (value)
                    {
                        values[3] = __Pyx_Arg_NewRef_FASTCALL(value);
                        kw_args--;
                    }
                    else if (unlikely(PyErr_Occurred()))
                        __PYX_ERR(0, 94, __pyx_L3_error)
                }
            }
            if (unlikely(kw_args > 0))
            {
                const Py_ssize_t kwd_pos_args = __pyx_nargs;
                if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values + 0, kwd_pos_args, "emd_with_flow") < 0))
                    __PYX_ERR(0, 94, __pyx_L3_error)
            }
        }
        else
        {
            switch (__pyx_nargs)
            {
            case 4:
                values[3] = __Pyx_Arg_FASTCALL(__pyx_args, 3);
                CYTHON_FALLTHROUGH;
            case 3:
                values[2] = __Pyx_Arg_FASTCALL(__pyx_args, 2);
                values[1] = __Pyx_Arg_FASTCALL(__pyx_args, 1);
                values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
                break;
            default:
                goto __pyx_L5_argtuple_error;
            }
        }
        __pyx_v_first_histogram = ((PyArrayObject *)values[0]);
        __pyx_v_second_histogram = ((PyArrayObject *)values[1]);
        __pyx_v_distance_matrix = ((PyArrayObject *)values[2]);
        __pyx_v_extra_mass_penalty = values[3];
    }
    goto __pyx_L6_skip;
__pyx_L5_argtuple_error:;
    __Pyx_RaiseArgtupleInvalid("emd_with_flow", 0, 3, 4, __pyx_nargs);
    __PYX_ERR(0, 94, __pyx_L3_error)
__pyx_L6_skip:;
    goto __pyx_L4_argument_unpacking_done;
__pyx_L3_error:;
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_AddTraceback("pyemd.emd.emd_with_flow", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __Pyx_RefNannyFinishContext();
    return NULL;
__pyx_L4_argument_unpacking_done:;
    if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_first_histogram), __pyx_ptype_5numpy_ndarray, 1, "first_histogram", 0)))
        __PYX_ERR(0, 94, __pyx_L1_error)
    if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_second_histogram), __pyx_ptype_5numpy_ndarray, 1, "second_histogram", 0)))
        __PYX_ERR(0, 95, __pyx_L1_error)
    if (unlikely(!__Pyx_ArgTypeTest(((PyObject *)__pyx_v_distance_matrix), __pyx_ptype_5numpy_ndarray, 1, "distance_matrix", 0)))
        __PYX_ERR(0, 96, __pyx_L1_error)
    __pyx_r = __pyx_pf_5pyemd_3emd_4emd_with_flow(__pyx_self, __pyx_v_first_histogram, __pyx_v_second_histogram, __pyx_v_distance_matrix, __pyx_v_extra_mass_penalty);

    /* function exit code */
    goto __pyx_L0;
__pyx_L1_error:;
    __pyx_r = NULL;
__pyx_L0:;
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

static PyObject *__pyx_pf_5pyemd_3emd_4emd_with_flow(CYTHON_UNUSED PyObject *__pyx_self, PyArrayObject *__pyx_v_first_histogram, PyArrayObject *__pyx_v_second_histogram, PyArrayObject *__pyx_v_distance_matrix, PyObject *__pyx_v_extra_mass_penalty)
{
    __Pyx_LocalBuf_ND __pyx_pybuffernd_distance_matrix;
    __Pyx_Buffer __pyx_pybuffer_distance_matrix;
    __Pyx_LocalBuf_ND __pyx_pybuffernd_first_histogram;
    __Pyx_Buffer __pyx_pybuffer_first_histogram;
    __Pyx_LocalBuf_ND __pyx_pybuffernd_second_histogram;
    __Pyx_Buffer __pyx_pybuffer_second_histogram;
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    int __pyx_t_4;
    std::vector<double> __pyx_t_5;
    std::vector<double> __pyx_t_6;
    std::vector<std::vector<double>> __pyx_t_7;
    double __pyx_t_8;
    std::pair<double, std::vector<std::vector<double>>> __pyx_t_9;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("emd_with_flow", 1);
    __pyx_pybuffer_first_histogram.pybuffer.buf = NULL;
    __pyx_pybuffer_first_histogram.refcount = 0;
    __pyx_pybuffernd_first_histogram.data = NULL;
    __pyx_pybuffernd_first_histogram.rcbuffer = &__pyx_pybuffer_first_histogram;
    __pyx_pybuffer_second_histogram.pybuffer.buf = NULL;
    __pyx_pybuffer_second_histogram.refcount = 0;
    __pyx_pybuffernd_second_histogram.data = NULL;
    __pyx_pybuffernd_second_histogram.rcbuffer = &__pyx_pybuffer_second_histogram;
    __pyx_pybuffer_distance_matrix.pybuffer.buf = NULL;
    __pyx_pybuffer_distance_matrix.refcount = 0;
    __pyx_pybuffernd_distance_matrix.data = NULL;
    __pyx_pybuffernd_distance_matrix.rcbuffer = &__pyx_pybuffer_distance_matrix;
    {
        __Pyx_BufFmt_StackElem __pyx_stack[1];
        if (unlikely(__Pyx_GetBufferAndValidate(&__pyx_pybuffernd_first_histogram.rcbuffer->pybuffer, (PyObject *)__pyx_v_first_histogram, &__Pyx_TypeInfo_nn___pyx_t_5numpy_float64_t, PyBUF_FORMAT | PyBUF_C_CONTIGUOUS, 1, 0, __pyx_stack) == -1))
            __PYX_ERR(0, 94, __pyx_L1_error)
    }
    __pyx_pybuffernd_first_histogram.diminfo[0].strides = __pyx_pybuffernd_first_histogram.rcbuffer->pybuffer.strides[0];
    __pyx_pybuffernd_first_histogram.diminfo[0].shape = __pyx_pybuffernd_first_histogram.rcbuffer->pybuffer.shape[0];
    {
        __Pyx_BufFmt_StackElem __pyx_stack[1];
        if (unlikely(__Pyx_GetBufferAndValidate(&__pyx_pybuffernd_second_histogram.rcbuffer->pybuffer, (PyObject *)__pyx_v_second_histogram, &__Pyx_TypeInfo_nn___pyx_t_5numpy_float64_t, PyBUF_FORMAT | PyBUF_C_CONTIGUOUS, 1, 0, __pyx_stack) == -1))
            __PYX_ERR(0, 94, __pyx_L1_error)
    }
    __pyx_pybuffernd_second_histogram.diminfo[0].strides = __pyx_pybuffernd_second_histogram.rcbuffer->pybuffer.strides[0];
    __pyx_pybuffernd_second_histogram.diminfo[0].shape = __pyx_pybuffernd_second_histogram.rcbuffer->pybuffer.shape[0];
    {
        __Pyx_BufFmt_StackElem __pyx_stack[1];
        if (unlikely(__Pyx_GetBufferAndValidate(&__pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer, (PyObject *)__pyx_v_distance_matrix, &__Pyx_TypeInfo_nn___pyx_t_5numpy_float64_t, PyBUF_FORMAT | PyBUF_C_CONTIGUOUS, 2, 0, __pyx_stack) == -1))
            __PYX_ERR(0, 94, __pyx_L1_error)
    }
    __pyx_pybuffernd_distance_matrix.diminfo[0].strides = __pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer.strides[0];
    __pyx_pybuffernd_distance_matrix.diminfo[0].shape = __pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer.shape[0];
    __pyx_pybuffernd_distance_matrix.diminfo[1].strides = __pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer.strides[1];
    __pyx_pybuffernd_distance_matrix.diminfo[1].shape = __pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer.shape[1];

    /* "pyemd/emd.pyx":131
     *         the same length.
     *     """
     *     _validate_emd_input(first_histogram, second_histogram, distance_matrix)             # <<<<<<<<<<<<<<
     *     return emd_hat_gd_metric_double_with_flow_wrapper(first_histogram,
     *                                                       second_histogram,
     */
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_validate_emd_input);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 131, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = NULL;
    __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_2)))
    {
        __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
        if (likely(__pyx_t_3))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
            __pyx_t_4 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[4] = {__pyx_t_3, ((PyObject *)__pyx_v_first_histogram), ((PyObject *)__pyx_v_second_histogram), ((PyObject *)__pyx_v_distance_matrix)};
        __pyx_t_1 = __Pyx_PyObject_FastCall(__pyx_t_2, __pyx_callargs + 1 - __pyx_t_4, 3 + __pyx_t_4);
        __Pyx_XDECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 131, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
    }
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;

    /* "pyemd/emd.pyx":132
     *     """
     *     _validate_emd_input(first_histogram, second_histogram, distance_matrix)
     *     return emd_hat_gd_metric_double_with_flow_wrapper(first_histogram,             # <<<<<<<<<<<<<<
     *                                                       second_histogram,
     *                                                       distance_matrix,
     */
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_5 = __pyx_convert_vector_from_py_double(((PyObject *)__pyx_v_first_histogram));
    if (unlikely(PyErr_Occurred()))
        __PYX_ERR(0, 132, __pyx_L1_error)

    /* "pyemd/emd.pyx":133
     *     _validate_emd_input(first_histogram, second_histogram, distance_matrix)
     *     return emd_hat_gd_metric_double_with_flow_wrapper(first_histogram,
     *                                                       second_histogram,             # <<<<<<<<<<<<<<
     *                                                       distance_matrix,
     *                                                       extra_mass_penalty)
     */
    __pyx_t_6 = __pyx_convert_vector_from_py_double(((PyObject *)__pyx_v_second_histogram));
    if (unlikely(PyErr_Occurred()))
        __PYX_ERR(0, 133, __pyx_L1_error)

    /* "pyemd/emd.pyx":134
     *     return emd_hat_gd_metric_double_with_flow_wrapper(first_histogram,
     *                                                       second_histogram,
     *                                                       distance_matrix,             # <<<<<<<<<<<<<<
     *                                                       extra_mass_penalty)
     *
     */
    __pyx_t_7 = __pyx_convert_vector_from_py_std_3a__3a_vector_3c_double_3e___(((PyObject *)__pyx_v_distance_matrix));
    if (unlikely(PyErr_Occurred()))
        __PYX_ERR(0, 134, __pyx_L1_error)

    /* "pyemd/emd.pyx":135
     *                                                       second_histogram,
     *                                                       distance_matrix,
     *                                                       extra_mass_penalty)             # <<<<<<<<<<<<<<
     *
     *
     */
    __pyx_t_8 = __pyx_PyFloat_AsDouble(__pyx_v_extra_mass_penalty);
    if (unlikely((__pyx_t_8 == (double)-1) && PyErr_Occurred()))
        __PYX_ERR(0, 135, __pyx_L1_error)

    /* "pyemd/emd.pyx":132
     *     """
     *     _validate_emd_input(first_histogram, second_histogram, distance_matrix)
     *     return emd_hat_gd_metric_double_with_flow_wrapper(first_histogram,             # <<<<<<<<<<<<<<
     *                                                       second_histogram,
     *                                                       distance_matrix,
     */
    try
    {
        __pyx_t_9 = emd_hat_gd_metric_double_with_flow_wrapper(__PYX_STD_MOVE_IF_SUPPORTED(__pyx_t_5), __PYX_STD_MOVE_IF_SUPPORTED(__pyx_t_6), __PYX_STD_MOVE_IF_SUPPORTED(__pyx_t_7), __pyx_t_8);
    }
    catch (...)
    {
        __Pyx_CppExn2PyErr();
        __PYX_ERR(0, 132, __pyx_L1_error)
    }
    __pyx_t_1 = __pyx_convert_pair_to_py_double____std_3a__3a_vector_3c_std_3a__3a_vector_3c_double_3e____3e___(__pyx_t_9);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 132, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_r = __pyx_t_1;
    __pyx_t_1 = 0;
    goto __pyx_L0;

/* "pyemd/emd.pyx":94
 *
 *
 * def emd_with_flow(np.ndarray[np.float64_t, ndim=1, mode="c"] first_histogram,             # <<<<<<<<<<<<<<
 *                   np.ndarray[np.float64_t, ndim=1, mode="c"] second_histogram,
 *                   np.ndarray[np.float64_t, ndim=2, mode="c"] distance_matrix,
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_3);
    {
        PyObject *__pyx_type, *__pyx_value, *__pyx_tb;
        __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
                __Pyx_ErrFetch(&__pyx_type, &__pyx_value, &__pyx_tb);
        __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer);
        __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_first_histogram.rcbuffer->pybuffer);
        __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_second_histogram.rcbuffer->pybuffer);
        __Pyx_ErrRestore(__pyx_type, __pyx_value, __pyx_tb);
    }
    __Pyx_AddTraceback("pyemd.emd.emd_with_flow", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = NULL;
    goto __pyx_L2;
__pyx_L0:;
    __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_distance_matrix.rcbuffer->pybuffer);
    __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_first_histogram.rcbuffer->pybuffer);
    __Pyx_SafeReleaseBuffer(&__pyx_pybuffernd_second_histogram.rcbuffer->pybuffer);
__pyx_L2:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "pyemd/emd.pyx":138
 *
 *
 * def euclidean_pairwise_distance_matrix(x):             # <<<<<<<<<<<<<<
 *     """Calculate the Euclidean pairwise distance matrix for a 1D array."""
 *     distance_matrix = np.abs(np.repeat(x, len(x)) - np.tile(x, len(x)))
 */

/* Python wrapper */
static PyObject *__pyx_pw_5pyemd_3emd_7euclidean_pairwise_distance_matrix(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                                                          PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                                                          PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_5pyemd_3emd_6euclidean_pairwise_distance_matrix, "Calculate the Euclidean pairwise distance matrix for a 1D array.");
static PyMethodDef __pyx_mdef_5pyemd_3emd_7euclidean_pairwise_distance_matrix = {"euclidean_pairwise_distance_matrix", (PyCFunction)(void *)(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_5pyemd_3emd_7euclidean_pairwise_distance_matrix, __Pyx_METH_FASTCALL | METH_KEYWORDS, __pyx_doc_5pyemd_3emd_6euclidean_pairwise_distance_matrix};
static PyObject *__pyx_pw_5pyemd_3emd_7euclidean_pairwise_distance_matrix(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                                                          PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                                                          PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
)
{
    PyObject *__pyx_v_x = 0;
#if !CYTHON_METH_FASTCALL
    CYTHON_UNUSED Py_ssize_t __pyx_nargs;
#endif
    CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
    PyObject *values[1] = {0};
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    PyObject *__pyx_r = 0;
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("euclidean_pairwise_distance_matrix (wrapper)", 0);
#if !CYTHON_METH_FASTCALL
#if CYTHON_ASSUME_SAFE_MACROS
    __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
#else
    __pyx_nargs = PyTuple_Size(__pyx_args);
    if (unlikely(__pyx_nargs < 0))
        return NULL;
#endif
#endif
    __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
    {
        PyObject **__pyx_pyargnames[] = {&__pyx_n_s_x, 0};
        if (__pyx_kwds)
        {
            Py_ssize_t kw_args;
            switch (__pyx_nargs)
            {
            case 1:
                values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
                CYTHON_FALLTHROUGH;
            case 0:
                break;
            default:
                goto __pyx_L5_argtuple_error;
            }
            kw_args = __Pyx_NumKwargs_FASTCALL(__pyx_kwds);
            switch (__pyx_nargs)
            {
            case 0:
                if (likely((values[0] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_x)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[0]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 138, __pyx_L3_error)
                else
                    goto __pyx_L5_argtuple_error;
            }
            if (unlikely(kw_args > 0))
            {
                const Py_ssize_t kwd_pos_args = __pyx_nargs;
                if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values + 0, kwd_pos_args, "euclidean_pairwise_distance_matrix") < 0))
                    __PYX_ERR(0, 138, __pyx_L3_error)
            }
        }
        else if (unlikely(__pyx_nargs != 1))
        {
            goto __pyx_L5_argtuple_error;
        }
        else
        {
            values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
        }
        __pyx_v_x = values[0];
    }
    goto __pyx_L6_skip;
__pyx_L5_argtuple_error:;
    __Pyx_RaiseArgtupleInvalid("euclidean_pairwise_distance_matrix", 1, 1, 1, __pyx_nargs);
    __PYX_ERR(0, 138, __pyx_L3_error)
__pyx_L6_skip:;
    goto __pyx_L4_argument_unpacking_done;
__pyx_L3_error:;
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_AddTraceback("pyemd.emd.euclidean_pairwise_distance_matrix", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __Pyx_RefNannyFinishContext();
    return NULL;
__pyx_L4_argument_unpacking_done:;
    __pyx_r = __pyx_pf_5pyemd_3emd_6euclidean_pairwise_distance_matrix(__pyx_self, __pyx_v_x);

    /* function exit code */
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

static PyObject *__pyx_pf_5pyemd_3emd_6euclidean_pairwise_distance_matrix(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_x)
{
    PyObject *__pyx_v_distance_matrix = NULL;
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    PyObject *__pyx_t_4 = NULL;
    PyObject *__pyx_t_5 = NULL;
    Py_ssize_t __pyx_t_6;
    PyObject *__pyx_t_7 = NULL;
    int __pyx_t_8;
    PyObject *__pyx_t_9 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("euclidean_pairwise_distance_matrix", 1);

    /* "pyemd/emd.pyx":140
     * def euclidean_pairwise_distance_matrix(x):
     *     """Calculate the Euclidean pairwise distance matrix for a 1D array."""
     *     distance_matrix = np.abs(np.repeat(x, len(x)) - np.tile(x, len(x)))             # <<<<<<<<<<<<<<
     *     return distance_matrix.reshape(len(x), len(x))
     *
     */
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_np);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_abs);
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_np);
    if (unlikely(!__pyx_t_4))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_repeat);
    if (unlikely(!__pyx_t_5))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_6 = PyObject_Length(__pyx_v_x);
    if (unlikely(__pyx_t_6 == ((Py_ssize_t)-1)))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __pyx_t_4 = PyInt_FromSsize_t(__pyx_t_6);
    if (unlikely(!__pyx_t_4))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_7 = NULL;
    __pyx_t_8 = 0;
#if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_5)))
    {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_7))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_5);
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_5, function);
            __pyx_t_8 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[3] = {__pyx_t_7, __pyx_v_x, __pyx_t_4};
        __pyx_t_2 = __Pyx_PyObject_FastCall(__pyx_t_5, __pyx_callargs + 1 - __pyx_t_8, 2 + __pyx_t_8);
        __Pyx_XDECREF(__pyx_t_7);
        __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_4);
        __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 140, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_5);
        __pyx_t_5 = 0;
    }
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_np);
    if (unlikely(!__pyx_t_4))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_tile);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_6 = PyObject_Length(__pyx_v_x);
    if (unlikely(__pyx_t_6 == ((Py_ssize_t)-1)))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __pyx_t_4 = PyInt_FromSsize_t(__pyx_t_6);
    if (unlikely(!__pyx_t_4))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_9 = NULL;
    __pyx_t_8 = 0;
#if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_7)))
    {
        __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_7);
        if (likely(__pyx_t_9))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_9);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
            __pyx_t_8 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[3] = {__pyx_t_9, __pyx_v_x, __pyx_t_4};
        __pyx_t_5 = __Pyx_PyObject_FastCall(__pyx_t_7, __pyx_callargs + 1 - __pyx_t_8, 2 + __pyx_t_8);
        __Pyx_XDECREF(__pyx_t_9);
        __pyx_t_9 = 0;
        __Pyx_DECREF(__pyx_t_4);
        __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_5))
            __PYX_ERR(0, 140, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_7);
        __pyx_t_7 = 0;
    }
    __pyx_t_7 = PyNumber_Subtract(__pyx_t_2, __pyx_t_5);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 140, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_5);
    __pyx_t_5 = 0;
    __pyx_t_5 = NULL;
    __pyx_t_8 = 0;
#if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_3)))
    {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_3);
        if (likely(__pyx_t_5))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_3);
            __Pyx_INCREF(__pyx_t_5);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_3, function);
            __pyx_t_8 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[2] = {__pyx_t_5, __pyx_t_7};
        __pyx_t_1 = __Pyx_PyObject_FastCall(__pyx_t_3, __pyx_callargs + 1 - __pyx_t_8, 1 + __pyx_t_8);
        __Pyx_XDECREF(__pyx_t_5);
        __pyx_t_5 = 0;
        __Pyx_DECREF(__pyx_t_7);
        __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 140, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_3);
        __pyx_t_3 = 0;
    }
    __pyx_v_distance_matrix = __pyx_t_1;
    __pyx_t_1 = 0;

    /* "pyemd/emd.pyx":141
     *     """Calculate the Euclidean pairwise distance matrix for a 1D array."""
     *     distance_matrix = np.abs(np.repeat(x, len(x)) - np.tile(x, len(x)))
     *     return distance_matrix.reshape(len(x), len(x))             # <<<<<<<<<<<<<<
     *
     *
     */
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_distance_matrix, __pyx_n_s_reshape);
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 141, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_6 = PyObject_Length(__pyx_v_x);
    if (unlikely(__pyx_t_6 == ((Py_ssize_t)-1)))
        __PYX_ERR(0, 141, __pyx_L1_error)
    __pyx_t_7 = PyInt_FromSsize_t(__pyx_t_6);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 141, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_6 = PyObject_Length(__pyx_v_x);
    if (unlikely(__pyx_t_6 == ((Py_ssize_t)-1)))
        __PYX_ERR(0, 141, __pyx_L1_error)
    __pyx_t_5 = PyInt_FromSsize_t(__pyx_t_6);
    if (unlikely(!__pyx_t_5))
        __PYX_ERR(0, 141, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_2 = NULL;
    __pyx_t_8 = 0;
#if CYTHON_UNPACK_METHODS
    if (likely(PyMethod_Check(__pyx_t_3)))
    {
        __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
        if (likely(__pyx_t_2))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_3);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_3, function);
            __pyx_t_8 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[3] = {__pyx_t_2, __pyx_t_7, __pyx_t_5};
        __pyx_t_1 = __Pyx_PyObject_FastCall(__pyx_t_3, __pyx_callargs + 1 - __pyx_t_8, 2 + __pyx_t_8);
        __Pyx_XDECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_7);
        __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_5);
        __pyx_t_5 = 0;
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 141, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_3);
        __pyx_t_3 = 0;
    }
    __pyx_r = __pyx_t_1;
    __pyx_t_1 = 0;
    goto __pyx_L0;

/* "pyemd/emd.pyx":138
 *
 *
 * def euclidean_pairwise_distance_matrix(x):             # <<<<<<<<<<<<<<
 *     """Calculate the Euclidean pairwise distance matrix for a 1D array."""
 *     distance_matrix = np.abs(np.repeat(x, len(x)) - np.tile(x, len(x)))
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_3);
    __Pyx_XDECREF(__pyx_t_4);
    __Pyx_XDECREF(__pyx_t_5);
    __Pyx_XDECREF(__pyx_t_7);
    __Pyx_XDECREF(__pyx_t_9);
    __Pyx_AddTraceback("pyemd.emd.euclidean_pairwise_distance_matrix", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = NULL;
__pyx_L0:;
    __Pyx_XDECREF(__pyx_v_distance_matrix);
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "pyemd/emd.pyx":148
 *     get_bins = np.histogram_bin_edges
 * else:
 *     def get_bins(a, bins=10, **kwargs):             # <<<<<<<<<<<<<<
 *         if isinstance(bins, str):
 *             hist, bins = np.histogram(a, bins=bins, **kwargs)
 */

/* Python wrapper */
static PyObject *__pyx_pw_5pyemd_3emd_9get_bins(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                                PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                                PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
static PyMethodDef __pyx_mdef_5pyemd_3emd_9get_bins = {"get_bins", (PyCFunction)(void *)(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_5pyemd_3emd_9get_bins, __Pyx_METH_FASTCALL | METH_KEYWORDS, 0};
static PyObject *__pyx_pw_5pyemd_3emd_9get_bins(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                                PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                                PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
)
{
    PyObject *__pyx_v_a = 0;
    PyObject *__pyx_v_bins = 0;
    PyObject *__pyx_v_kwargs = 0;
#if !CYTHON_METH_FASTCALL
    CYTHON_UNUSED Py_ssize_t __pyx_nargs;
#endif
    CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
    PyObject *values[2] = {0, 0};
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    PyObject *__pyx_r = 0;
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("get_bins (wrapper)", 0);
#if !CYTHON_METH_FASTCALL
#if CYTHON_ASSUME_SAFE_MACROS
    __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
#else
    __pyx_nargs = PyTuple_Size(__pyx_args);
    if (unlikely(__pyx_nargs < 0))
        return NULL;
#endif
#endif
    __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
    __pyx_v_kwargs = PyDict_New();
    if (unlikely(!__pyx_v_kwargs))
        return NULL;
    __Pyx_GOTREF(__pyx_v_kwargs);
    {
        PyObject **__pyx_pyargnames[] = {&__pyx_n_s_a, &__pyx_n_s_bins, 0};
        values[1] = __Pyx_Arg_NewRef_FASTCALL(((PyObject *)((PyObject *)__pyx_int_10)));
        if (__pyx_kwds)
        {
            Py_ssize_t kw_args;
            switch (__pyx_nargs)
            {
            case 2:
                values[1] = __Pyx_Arg_FASTCALL(__pyx_args, 1);
                CYTHON_FALLTHROUGH;
            case 1:
                values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
                CYTHON_FALLTHROUGH;
            case 0:
                break;
            default:
                goto __pyx_L5_argtuple_error;
            }
            kw_args = __Pyx_NumKwargs_FASTCALL(__pyx_kwds);
            switch (__pyx_nargs)
            {
            case 0:
                if (likely((values[0] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_a)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[0]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 148, __pyx_L3_error)
                else
                    goto __pyx_L5_argtuple_error;
                CYTHON_FALLTHROUGH;
            case 1:
                if (kw_args > 0)
                {
                    PyObject *value = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_bins);
                    if (value)
                    {
                        values[1] = __Pyx_Arg_NewRef_FASTCALL(value);
                        kw_args--;
                    }
                    else if (unlikely(PyErr_Occurred()))
                        __PYX_ERR(0, 148, __pyx_L3_error)
                }
            }
            if (unlikely(kw_args > 0))
            {
                const Py_ssize_t kwd_pos_args = __pyx_nargs;
                if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, __pyx_v_kwargs, values + 0, kwd_pos_args, "get_bins") < 0))
                    __PYX_ERR(0, 148, __pyx_L3_error)
            }
        }
        else
        {
            switch (__pyx_nargs)
            {
            case 2:
                values[1] = __Pyx_Arg_FASTCALL(__pyx_args, 1);
                CYTHON_FALLTHROUGH;
            case 1:
                values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
                break;
            default:
                goto __pyx_L5_argtuple_error;
            }
        }
        __pyx_v_a = values[0];
        __pyx_v_bins = values[1];
    }
    goto __pyx_L6_skip;
__pyx_L5_argtuple_error:;
    __Pyx_RaiseArgtupleInvalid("get_bins", 0, 1, 2, __pyx_nargs);
    __PYX_ERR(0, 148, __pyx_L3_error)
__pyx_L6_skip:;
    goto __pyx_L4_argument_unpacking_done;
__pyx_L3_error:;
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_DECREF(__pyx_v_kwargs);
    __pyx_v_kwargs = 0;
    __Pyx_AddTraceback("pyemd.emd.get_bins", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __Pyx_RefNannyFinishContext();
    return NULL;
__pyx_L4_argument_unpacking_done:;
    __pyx_r = __pyx_pf_5pyemd_3emd_8get_bins(__pyx_self, __pyx_v_a, __pyx_v_bins, __pyx_v_kwargs);

    /* function exit code */
    __Pyx_DECREF(__pyx_v_kwargs);
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

static PyObject *__pyx_pf_5pyemd_3emd_8get_bins(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_a, PyObject *__pyx_v_bins, PyObject *__pyx_v_kwargs)
{
    CYTHON_UNUSED PyObject *__pyx_v_hist = NULL;
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations int __pyx_t_1;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    PyObject *__pyx_t_4 = NULL;
    PyObject *__pyx_t_5 = NULL;
    PyObject *(*__pyx_t_6)(PyObject *);
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("get_bins", 0);
    __Pyx_INCREF(__pyx_v_bins);

    /* "pyemd/emd.pyx":149
     * else:
     *     def get_bins(a, bins=10, **kwargs):
     *         if isinstance(bins, str):             # <<<<<<<<<<<<<<
     *             hist, bins = np.histogram(a, bins=bins, **kwargs)
     *         return bins
     */
    __pyx_t_1 = PyUnicode_Check(__pyx_v_bins);
    if (__pyx_t_1)
    {

        /* "pyemd/emd.pyx":150
         *     def get_bins(a, bins=10, **kwargs):
         *         if isinstance(bins, str):
         *             hist, bins = np.histogram(a, bins=bins, **kwargs)             # <<<<<<<<<<<<<<
         *         return bins
         *
         */
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_np);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 150, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_histogram);
        if (unlikely(!__pyx_t_3))
            __PYX_ERR(0, 150, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __pyx_t_2 = PyTuple_New(1);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 150, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_INCREF(__pyx_v_a);
        __Pyx_GIVEREF(__pyx_v_a);
        if (__Pyx_PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_a))
            __PYX_ERR(0, 150, __pyx_L1_error);
        __pyx_t_5 = __Pyx_PyDict_NewPresized(1);
        if (unlikely(!__pyx_t_5))
            __PYX_ERR(0, 150, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_bins, __pyx_v_bins) < 0)
            __PYX_ERR(0, 150, __pyx_L1_error)
        __pyx_t_4 = __pyx_t_5;
        __pyx_t_5 = 0;
        if (__Pyx_MergeKeywords(__pyx_t_4, __pyx_v_kwargs) < 0)
            __PYX_ERR(0, 150, __pyx_L1_error)
        __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_2, __pyx_t_4);
        if (unlikely(!__pyx_t_5))
            __PYX_ERR(0, 150, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_4);
        __pyx_t_4 = 0;
        if ((likely(PyTuple_CheckExact(__pyx_t_5))) || (PyList_CheckExact(__pyx_t_5)))
        {
            PyObject *sequence = __pyx_t_5;
            Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
            if (unlikely(size != 2))
            {
                if (size > 2)
                    __Pyx_RaiseTooManyValuesError(2);
                else if (size >= 0)
                    __Pyx_RaiseNeedMoreValuesError(size);
                __PYX_ERR(0, 150, __pyx_L1_error)
            }
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
            if (likely(PyTuple_CheckExact(sequence)))
            {
                __pyx_t_4 = PyTuple_GET_ITEM(sequence, 0);
                __pyx_t_2 = PyTuple_GET_ITEM(sequence, 1);
            }
            else
            {
                __pyx_t_4 = PyList_GET_ITEM(sequence, 0);
                __pyx_t_2 = PyList_GET_ITEM(sequence, 1);
            }
            __Pyx_INCREF(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_2);
#else
            __pyx_t_4 = PySequence_ITEM(sequence, 0);
            if (unlikely(!__pyx_t_4))
                __PYX_ERR(0, 150, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_2 = PySequence_ITEM(sequence, 1);
            if (unlikely(!__pyx_t_2))
                __PYX_ERR(0, 150, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_2);
#endif
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = 0;
        }
        else
        {
            Py_ssize_t index = -1;
            __pyx_t_3 = PyObject_GetIter(__pyx_t_5);
            if (unlikely(!__pyx_t_3))
                __PYX_ERR(0, 150, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_3);
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = 0;
            __pyx_t_6 = __Pyx_PyObject_GetIterNextFunc(__pyx_t_3);
            index = 0;
            __pyx_t_4 = __pyx_t_6(__pyx_t_3);
            if (unlikely(!__pyx_t_4))
                goto __pyx_L4_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_4);
            index = 1;
            __pyx_t_2 = __pyx_t_6(__pyx_t_3);
            if (unlikely(!__pyx_t_2))
                goto __pyx_L4_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_2);
            if (__Pyx_IternextUnpackEndCheck(__pyx_t_6(__pyx_t_3), 2) < 0)
                __PYX_ERR(0, 150, __pyx_L1_error)
            __pyx_t_6 = NULL;
            __Pyx_DECREF(__pyx_t_3);
            __pyx_t_3 = 0;
            goto __pyx_L5_unpacking_done;
        __pyx_L4_unpacking_failed:;
            __Pyx_DECREF(__pyx_t_3);
            __pyx_t_3 = 0;
            __pyx_t_6 = NULL;
            if (__Pyx_IterFinish() == 0)
                __Pyx_RaiseNeedMoreValuesError(index);
            __PYX_ERR(0, 150, __pyx_L1_error)
        __pyx_L5_unpacking_done:;
        }
        __pyx_v_hist = __pyx_t_4;
        __pyx_t_4 = 0;
        __Pyx_DECREF_SET(__pyx_v_bins, __pyx_t_2);
        __pyx_t_2 = 0;

        /* "pyemd/emd.pyx":149
         * else:
         *     def get_bins(a, bins=10, **kwargs):
         *         if isinstance(bins, str):             # <<<<<<<<<<<<<<
         *             hist, bins = np.histogram(a, bins=bins, **kwargs)
         *         return bins
         */
    }

    /* "pyemd/emd.pyx":151
     *         if isinstance(bins, str):
     *             hist, bins = np.histogram(a, bins=bins, **kwargs)
     *         return bins             # <<<<<<<<<<<<<<
     *
     *
     */
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_bins);
    __pyx_r = __pyx_v_bins;
    goto __pyx_L0;

/* "pyemd/emd.pyx":148
 *     get_bins = np.histogram_bin_edges
 * else:
 *     def get_bins(a, bins=10, **kwargs):             # <<<<<<<<<<<<<<
 *         if isinstance(bins, str):
 *             hist, bins = np.histogram(a, bins=bins, **kwargs)
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_3);
    __Pyx_XDECREF(__pyx_t_4);
    __Pyx_XDECREF(__pyx_t_5);
    __Pyx_AddTraceback("pyemd.emd.get_bins", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = NULL;
__pyx_L0:;
    __Pyx_XDECREF(__pyx_v_hist);
    __Pyx_XDECREF(__pyx_v_bins);
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* "pyemd/emd.pyx":154
 *
 *
 * def emd_samples(first_array,             # <<<<<<<<<<<<<<
 *                 second_array,
 *                 extra_mass_penalty=DEFAULT_EXTRA_MASS_PENALTY,
 */

static PyObject *__pyx_pf_5pyemd_3emd_16__defaults__(CYTHON_UNUSED PyObject *__pyx_self)
{
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("__defaults__", 1);
    __Pyx_XDECREF(__pyx_r);

    /* "pyemd/emd.pyx":160
     *                 normalized=True,
     *                 bins='auto',
     *                 range=None):             # <<<<<<<<<<<<<<
     *     u"""Return the EMD between the histograms of two arrays.
     *
     */
    __pyx_t_1 = PyTuple_New(5);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 154, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_INCREF(__Pyx_CyFunction_Defaults(__pyx_defaults2, __pyx_self)->__pyx_arg_extra_mass_penalty);
    __Pyx_GIVEREF(__Pyx_CyFunction_Defaults(__pyx_defaults2, __pyx_self)->__pyx_arg_extra_mass_penalty);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __Pyx_CyFunction_Defaults(__pyx_defaults2, __pyx_self)->__pyx_arg_extra_mass_penalty))
        __PYX_ERR(0, 154, __pyx_L1_error);
    __Pyx_INCREF(((PyObject *)__pyx_n_u_euclidean));
    __Pyx_GIVEREF(((PyObject *)__pyx_n_u_euclidean));
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 1, ((PyObject *)__pyx_n_u_euclidean)))
        __PYX_ERR(0, 154, __pyx_L1_error);
    __Pyx_INCREF(((PyObject *)Py_True));
    __Pyx_GIVEREF(((PyObject *)Py_True));
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 2, ((PyObject *)Py_True)))
        __PYX_ERR(0, 154, __pyx_L1_error);
    __Pyx_INCREF(((PyObject *)__pyx_n_u_auto));
    __Pyx_GIVEREF(((PyObject *)__pyx_n_u_auto));
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 3, ((PyObject *)__pyx_n_u_auto)))
        __PYX_ERR(0, 154, __pyx_L1_error);
    __Pyx_INCREF(Py_None);
    __Pyx_GIVEREF(Py_None);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 4, Py_None))
        __PYX_ERR(0, 154, __pyx_L1_error);

    /* "pyemd/emd.pyx":154
     *
     *
     * def emd_samples(first_array,             # <<<<<<<<<<<<<<
     *                 second_array,
     *                 extra_mass_penalty=DEFAULT_EXTRA_MASS_PENALTY,
     */
    __pyx_t_2 = PyTuple_New(2);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 154, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_GIVEREF(__pyx_t_1);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_1))
        __PYX_ERR(0, 154, __pyx_L1_error);
    __Pyx_INCREF(Py_None);
    __Pyx_GIVEREF(Py_None);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_2, 1, Py_None))
        __PYX_ERR(0, 154, __pyx_L1_error);
    __pyx_t_1 = 0;
    __pyx_r = __pyx_t_2;
    __pyx_t_2 = 0;
    goto __pyx_L0;

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_AddTraceback("pyemd.emd.__defaults__", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = NULL;
__pyx_L0:;
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

/* Python wrapper */
static PyObject *__pyx_pw_5pyemd_3emd_11emd_samples(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                                    PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                                    PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
); /*proto*/
PyDoc_STRVAR(__pyx_doc_5pyemd_3emd_10emd_samples, "Return the EMD between the histograms of two arrays.\n\n    See ``emd()`` for more information about the EMD.\n\n    Note:\n        Pairwise ground distances are taken from the center of the bins.\n\n    Arguments:\n        first_array (Iterable): An array of samples used to generate a\n            histogram.\n        second_array (Iterable): An array of samples used to generate a\n            histogram.\n\n    Keyword Arguments:\n        extra_mass_penalty (float): The penalty for extra mass. If you want the\n            resulting distance to be a metric, it should be at least half the\n            diameter of the space (maximum possible distance between any two\n            points). If you want partial matching you can set it to zero (but\n            then the resulting distance is not guaranteed to be a metric). The\n            default value is -1, which means the maximum value in the distance\n            matrix is used.\n        distance (string or function): A string or function implementing\n            a metric on a 1D ``np.ndarray``. Defaults to the Euclidean distance.\n            Currently limited to 'euclidean' or your own function, which must\n            take a 1D array and return a square 2D array of pairwise distances.\n        normalized (boolean): If true (default), treat histograms as fractions\n            of the dataset. If false, treat histograms as counts. In the latter\n            case the EMD will vary greatly by array length.\n        bins (int or string): The number of bins to include in the generated\n            histogram. If a string, must be one of the bin selection algorithms\n            accepted by ``np.histogram()``. Defaults to 'auto', which gives the\n            maximum of the 'sturges' and 'fd' estimators.\n        range (tuple(int, int)): The lower and upper range of the bins, passed\n            to ``numpy.histogram()``. Defaults to the range of the union of\n            ``first_array`` and `second_array``.` Note: if the gi"
                                                  "ven range is\n            not a superset of the default range, no warning will be given.\n\n    Returns:\n        float: The EMD value between the histograms of ``first_array`` and\n        ``second_array``.\n    ");
static PyMethodDef __pyx_mdef_5pyemd_3emd_11emd_samples = {"emd_samples", (PyCFunction)(void *)(__Pyx_PyCFunction_FastCallWithKeywords)__pyx_pw_5pyemd_3emd_11emd_samples, __Pyx_METH_FASTCALL | METH_KEYWORDS, __pyx_doc_5pyemd_3emd_10emd_samples};
static PyObject *__pyx_pw_5pyemd_3emd_11emd_samples(PyObject *__pyx_self,
#if CYTHON_METH_FASTCALL
                                                    PyObject *const *__pyx_args, Py_ssize_t __pyx_nargs, PyObject *__pyx_kwds
#else
                                                    PyObject *__pyx_args, PyObject *__pyx_kwds
#endif
)
{
    PyObject *__pyx_v_first_array = 0;
    PyObject *__pyx_v_second_array = 0;
    PyObject *__pyx_v_extra_mass_penalty = 0;
    PyObject *__pyx_v_distance = 0;
    PyObject *__pyx_v_normalized = 0;
    PyObject *__pyx_v_bins = 0;
    PyObject *__pyx_v_range = 0;
#if !CYTHON_METH_FASTCALL
    CYTHON_UNUSED Py_ssize_t __pyx_nargs;
#endif
    CYTHON_UNUSED PyObject *const *__pyx_kwvalues;
    PyObject *values[7] = {0, 0, 0, 0, 0, 0, 0};
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    PyObject *__pyx_r = 0;
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("emd_samples (wrapper)", 0);
#if !CYTHON_METH_FASTCALL
#if CYTHON_ASSUME_SAFE_MACROS
    __pyx_nargs = PyTuple_GET_SIZE(__pyx_args);
#else
    __pyx_nargs = PyTuple_Size(__pyx_args);
    if (unlikely(__pyx_nargs < 0))
        return NULL;
#endif
#endif
    __pyx_kwvalues = __Pyx_KwValues_FASTCALL(__pyx_args, __pyx_nargs);
    {
        PyObject **__pyx_pyargnames[] = {&__pyx_n_s_first_array, &__pyx_n_s_second_array, &__pyx_n_s_extra_mass_penalty, &__pyx_n_s_distance, &__pyx_n_s_normalized, &__pyx_n_s_bins, &__pyx_n_s_range, 0};
        __pyx_defaults2 *__pyx_dynamic_args = __Pyx_CyFunction_Defaults(__pyx_defaults2, __pyx_self);
        values[2] = __Pyx_Arg_NewRef_FASTCALL(__pyx_dynamic_args->__pyx_arg_extra_mass_penalty);
        values[3] = __Pyx_Arg_NewRef_FASTCALL(((PyObject *)((PyObject *)__pyx_n_u_euclidean)));
        values[4] = __Pyx_Arg_NewRef_FASTCALL(((PyObject *)((PyObject *)Py_True)));
        values[5] = __Pyx_Arg_NewRef_FASTCALL(((PyObject *)((PyObject *)__pyx_n_u_auto)));

        /* "pyemd/emd.pyx":160
         *                 normalized=True,
         *                 bins='auto',
         *                 range=None):             # <<<<<<<<<<<<<<
         *     u"""Return the EMD between the histograms of two arrays.
         *
         */
        values[6] = __Pyx_Arg_NewRef_FASTCALL(((PyObject *)Py_None));
        if (__pyx_kwds)
        {
            Py_ssize_t kw_args;
            switch (__pyx_nargs)
            {
            case 7:
                values[6] = __Pyx_Arg_FASTCALL(__pyx_args, 6);
                CYTHON_FALLTHROUGH;
            case 6:
                values[5] = __Pyx_Arg_FASTCALL(__pyx_args, 5);
                CYTHON_FALLTHROUGH;
            case 5:
                values[4] = __Pyx_Arg_FASTCALL(__pyx_args, 4);
                CYTHON_FALLTHROUGH;
            case 4:
                values[3] = __Pyx_Arg_FASTCALL(__pyx_args, 3);
                CYTHON_FALLTHROUGH;
            case 3:
                values[2] = __Pyx_Arg_FASTCALL(__pyx_args, 2);
                CYTHON_FALLTHROUGH;
            case 2:
                values[1] = __Pyx_Arg_FASTCALL(__pyx_args, 1);
                CYTHON_FALLTHROUGH;
            case 1:
                values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
                CYTHON_FALLTHROUGH;
            case 0:
                break;
            default:
                goto __pyx_L5_argtuple_error;
            }
            kw_args = __Pyx_NumKwargs_FASTCALL(__pyx_kwds);
            switch (__pyx_nargs)
            {
            case 0:
                if (likely((values[0] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_first_array)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[0]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 154, __pyx_L3_error)
                else
                    goto __pyx_L5_argtuple_error;
                CYTHON_FALLTHROUGH;
            case 1:
                if (likely((values[1] = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_second_array)) != 0))
                {
                    (void)__Pyx_Arg_NewRef_FASTCALL(values[1]);
                    kw_args--;
                }
                else if (unlikely(PyErr_Occurred()))
                    __PYX_ERR(0, 154, __pyx_L3_error)
                else
                {
                    __Pyx_RaiseArgtupleInvalid("emd_samples", 0, 2, 7, 1);
                    __PYX_ERR(0, 154, __pyx_L3_error)
                }
                CYTHON_FALLTHROUGH;
            case 2:
                if (kw_args > 0)
                {
                    PyObject *value = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_extra_mass_penalty);
                    if (value)
                    {
                        values[2] = __Pyx_Arg_NewRef_FASTCALL(value);
                        kw_args--;
                    }
                    else if (unlikely(PyErr_Occurred()))
                        __PYX_ERR(0, 154, __pyx_L3_error)
                }
                CYTHON_FALLTHROUGH;
            case 3:
                if (kw_args > 0)
                {
                    PyObject *value = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_distance);
                    if (value)
                    {
                        values[3] = __Pyx_Arg_NewRef_FASTCALL(value);
                        kw_args--;
                    }
                    else if (unlikely(PyErr_Occurred()))
                        __PYX_ERR(0, 154, __pyx_L3_error)
                }
                CYTHON_FALLTHROUGH;
            case 4:
                if (kw_args > 0)
                {
                    PyObject *value = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_normalized);
                    if (value)
                    {
                        values[4] = __Pyx_Arg_NewRef_FASTCALL(value);
                        kw_args--;
                    }
                    else if (unlikely(PyErr_Occurred()))
                        __PYX_ERR(0, 154, __pyx_L3_error)
                }
                CYTHON_FALLTHROUGH;
            case 5:
                if (kw_args > 0)
                {
                    PyObject *value = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_bins);
                    if (value)
                    {
                        values[5] = __Pyx_Arg_NewRef_FASTCALL(value);
                        kw_args--;
                    }
                    else if (unlikely(PyErr_Occurred()))
                        __PYX_ERR(0, 154, __pyx_L3_error)
                }
                CYTHON_FALLTHROUGH;
            case 6:
                if (kw_args > 0)
                {
                    PyObject *value = __Pyx_GetKwValue_FASTCALL(__pyx_kwds, __pyx_kwvalues, __pyx_n_s_range);
                    if (value)
                    {
                        values[6] = __Pyx_Arg_NewRef_FASTCALL(value);
                        kw_args--;
                    }
                    else if (unlikely(PyErr_Occurred()))
                        __PYX_ERR(0, 154, __pyx_L3_error)
                }
            }
            if (unlikely(kw_args > 0))
            {
                const Py_ssize_t kwd_pos_args = __pyx_nargs;
                if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_kwvalues, __pyx_pyargnames, 0, values + 0, kwd_pos_args, "emd_samples") < 0))
                    __PYX_ERR(0, 154, __pyx_L3_error)
            }
        }
        else
        {
            switch (__pyx_nargs)
            {
            case 7:
                values[6] = __Pyx_Arg_FASTCALL(__pyx_args, 6);
                CYTHON_FALLTHROUGH;
            case 6:
                values[5] = __Pyx_Arg_FASTCALL(__pyx_args, 5);
                CYTHON_FALLTHROUGH;
            case 5:
                values[4] = __Pyx_Arg_FASTCALL(__pyx_args, 4);
                CYTHON_FALLTHROUGH;
            case 4:
                values[3] = __Pyx_Arg_FASTCALL(__pyx_args, 3);
                CYTHON_FALLTHROUGH;
            case 3:
                values[2] = __Pyx_Arg_FASTCALL(__pyx_args, 2);
                CYTHON_FALLTHROUGH;
            case 2:
                values[1] = __Pyx_Arg_FASTCALL(__pyx_args, 1);
                values[0] = __Pyx_Arg_FASTCALL(__pyx_args, 0);
                break;
            default:
                goto __pyx_L5_argtuple_error;
            }
        }
        __pyx_v_first_array = values[0];
        __pyx_v_second_array = values[1];
        __pyx_v_extra_mass_penalty = values[2];
        __pyx_v_distance = values[3];
        __pyx_v_normalized = values[4];
        __pyx_v_bins = values[5];
        __pyx_v_range = values[6];
    }
    goto __pyx_L6_skip;
__pyx_L5_argtuple_error:;
    __Pyx_RaiseArgtupleInvalid("emd_samples", 0, 2, 7, __pyx_nargs);
    __PYX_ERR(0, 154, __pyx_L3_error)
__pyx_L6_skip:;
    goto __pyx_L4_argument_unpacking_done;
__pyx_L3_error:;
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_AddTraceback("pyemd.emd.emd_samples", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __Pyx_RefNannyFinishContext();
    return NULL;
__pyx_L4_argument_unpacking_done:;
    __pyx_r = __pyx_pf_5pyemd_3emd_10emd_samples(__pyx_self, __pyx_v_first_array, __pyx_v_second_array, __pyx_v_extra_mass_penalty, __pyx_v_distance, __pyx_v_normalized, __pyx_v_bins, __pyx_v_range);

    /* "pyemd/emd.pyx":154
     *
     *
     * def emd_samples(first_array,             # <<<<<<<<<<<<<<
     *                 second_array,
     *                 extra_mass_penalty=DEFAULT_EXTRA_MASS_PENALTY,
     */

    /* function exit code */
    {
        Py_ssize_t __pyx_temp;
        for (__pyx_temp = 0; __pyx_temp < (Py_ssize_t)(sizeof(values) / sizeof(values[0])); ++__pyx_temp)
        {
            __Pyx_Arg_XDECREF_FASTCALL(values[__pyx_temp]);
        }
    }
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

static PyObject *__pyx_pf_5pyemd_3emd_10emd_samples(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_first_array, PyObject *__pyx_v_second_array, PyObject *__pyx_v_extra_mass_penalty, PyObject *__pyx_v_distance, PyObject *__pyx_v_normalized, PyObject *__pyx_v_bins, PyObject *__pyx_v_range)
{
    PyObject *__pyx_v_first_histogram = NULL;
    PyObject *__pyx_v_bin_edges = NULL;
    PyObject *__pyx_v_second_histogram = NULL;
    CYTHON_UNUSED PyObject *__pyx_v__ = NULL;
    PyObject *__pyx_v_bin_locations = NULL;
    PyObject *__pyx_v_distance_matrix = NULL;
    PyObject *__pyx_r = NULL;
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    int __pyx_t_4;
    int __pyx_t_5;
    int __pyx_t_6;
    PyObject *__pyx_t_7 = NULL;
    PyObject *__pyx_t_8 = NULL;
    PyObject *(*__pyx_t_9)(PyObject *);
    Py_ssize_t __pyx_t_10;
    Py_ssize_t __pyx_t_11;
    std::vector<double> __pyx_t_12;
    std::vector<double> __pyx_t_13;
    std::vector<std::vector<double>> __pyx_t_14;
    double __pyx_t_15;
    double __pyx_t_16;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("emd_samples", 0);
    __Pyx_INCREF(__pyx_v_first_array);
    __Pyx_INCREF(__pyx_v_second_array);
    __Pyx_INCREF(__pyx_v_distance);
    __Pyx_INCREF(__pyx_v_bins);
    __Pyx_INCREF(__pyx_v_range);

    /* "pyemd/emd.pyx":202
     *         ``second_array``.
     *     """
     *     first_array = np.array(first_array)             # <<<<<<<<<<<<<<
     *     second_array = np.array(second_array)
     *     # Validate arrays
     */
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_np);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 202, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_array);
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 202, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_2 = NULL;
    __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_3)))
    {
        __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
        if (likely(__pyx_t_2))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_3);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_3, function);
            __pyx_t_4 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_first_array};
        __pyx_t_1 = __Pyx_PyObject_FastCall(__pyx_t_3, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
        __Pyx_XDECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 202, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_3);
        __pyx_t_3 = 0;
    }
    __Pyx_DECREF_SET(__pyx_v_first_array, __pyx_t_1);
    __pyx_t_1 = 0;

    /* "pyemd/emd.pyx":203
     *     """
     *     first_array = np.array(first_array)
     *     second_array = np.array(second_array)             # <<<<<<<<<<<<<<
     *     # Validate arrays
     *     if not (first_array.size > 0 and second_array.size > 0):
     */
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_np);
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 203, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_array);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 203, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_3 = NULL;
    __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_2)))
    {
        __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
        if (likely(__pyx_t_3))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
            __pyx_t_4 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_second_array};
        __pyx_t_1 = __Pyx_PyObject_FastCall(__pyx_t_2, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
        __Pyx_XDECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 203, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
    }
    __Pyx_DECREF_SET(__pyx_v_second_array, __pyx_t_1);
    __pyx_t_1 = 0;

    /* "pyemd/emd.pyx":205
     *     second_array = np.array(second_array)
     *     # Validate arrays
     *     if not (first_array.size > 0 and second_array.size > 0):             # <<<<<<<<<<<<<<
     *         raise ValueError('Arrays of samples cannot be empty.')
     *     # Get the default range
     */
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_first_array, __pyx_n_s_size);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 205, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = PyObject_RichCompare(__pyx_t_1, __pyx_int_0, Py_GT);
    __Pyx_XGOTREF(__pyx_t_2);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 205, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_2);
    if (unlikely((__pyx_t_6 < 0)))
        __PYX_ERR(0, 205, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    if (__pyx_t_6)
    {
    }
    else
    {
        __pyx_t_5 = __pyx_t_6;
        goto __pyx_L4_bool_binop_done;
    }
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_second_array, __pyx_n_s_size);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 205, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = PyObject_RichCompare(__pyx_t_2, __pyx_int_0, Py_GT);
    __Pyx_XGOTREF(__pyx_t_1);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 205, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_1);
    if (unlikely((__pyx_t_6 < 0)))
        __PYX_ERR(0, 205, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __pyx_t_5 = __pyx_t_6;
__pyx_L4_bool_binop_done:;
    __pyx_t_6 = (!__pyx_t_5);
    if (unlikely(__pyx_t_6))
    {

        /* "pyemd/emd.pyx":206
         *     # Validate arrays
         *     if not (first_array.size > 0 and second_array.size > 0):
         *         raise ValueError('Arrays of samples cannot be empty.')             # <<<<<<<<<<<<<<
         *     # Get the default range
         *     if range is None:
         */
        __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_ValueError, __pyx_tuple__5, NULL);
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 206, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_Raise(__pyx_t_1, 0, 0, 0);
        __Pyx_DECREF(__pyx_t_1);
        __pyx_t_1 = 0;
        __PYX_ERR(0, 206, __pyx_L1_error)

        /* "pyemd/emd.pyx":205
         *     second_array = np.array(second_array)
         *     # Validate arrays
         *     if not (first_array.size > 0 and second_array.size > 0):             # <<<<<<<<<<<<<<
         *         raise ValueError('Arrays of samples cannot be empty.')
         *     # Get the default range
         */
    }

    /* "pyemd/emd.pyx":208
     *         raise ValueError('Arrays of samples cannot be empty.')
     *     # Get the default range
     *     if range is None:             # <<<<<<<<<<<<<<
     *         range = (min(np.min(first_array), np.min(second_array)),
     *                  max(np.max(first_array), np.max(second_array)))
     */
    __pyx_t_6 = (__pyx_v_range == Py_None);
    if (__pyx_t_6)
    {

        /* "pyemd/emd.pyx":209
         *     # Get the default range
         *     if range is None:
         *         range = (min(np.min(first_array), np.min(second_array)),             # <<<<<<<<<<<<<<
         *                  max(np.max(first_array), np.max(second_array)))
         *     # Get bin edges using both arrays
         */
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_np);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 209, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_min);
        if (unlikely(!__pyx_t_3))
            __PYX_ERR(0, 209, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __pyx_t_2 = NULL;
        __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
        if (unlikely(PyMethod_Check(__pyx_t_3)))
        {
            __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
            if (likely(__pyx_t_2))
            {
                PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_3);
                __Pyx_INCREF(__pyx_t_2);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_3, function);
                __pyx_t_4 = 1;
            }
        }
#endif
        {
            PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_second_array};
            __pyx_t_1 = __Pyx_PyObject_FastCall(__pyx_t_3, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
            __Pyx_XDECREF(__pyx_t_2);
            __pyx_t_2 = 0;
            if (unlikely(!__pyx_t_1))
                __PYX_ERR(0, 209, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_3);
            __pyx_t_3 = 0;
        }
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_np);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 209, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_min);
        if (unlikely(!__pyx_t_7))
            __PYX_ERR(0, 209, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __pyx_t_2 = NULL;
        __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
        if (unlikely(PyMethod_Check(__pyx_t_7)))
        {
            __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_7);
            if (likely(__pyx_t_2))
            {
                PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_7);
                __Pyx_INCREF(__pyx_t_2);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_7, function);
                __pyx_t_4 = 1;
            }
        }
#endif
        {
            PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_v_first_array};
            __pyx_t_3 = __Pyx_PyObject_FastCall(__pyx_t_7, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
            __Pyx_XDECREF(__pyx_t_2);
            __pyx_t_2 = 0;
            if (unlikely(!__pyx_t_3))
                __PYX_ERR(0, 209, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_3);
            __Pyx_DECREF(__pyx_t_7);
            __pyx_t_7 = 0;
        }
        __pyx_t_2 = PyObject_RichCompare(__pyx_t_1, __pyx_t_3, Py_LT);
        __Pyx_XGOTREF(__pyx_t_2);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 209, __pyx_L1_error)
        __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_2);
        if (unlikely((__pyx_t_6 < 0)))
            __PYX_ERR(0, 209, __pyx_L1_error)
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        if (__pyx_t_6)
        {
            __Pyx_INCREF(__pyx_t_1);
            __pyx_t_7 = __pyx_t_1;
        }
        else
        {
            __Pyx_INCREF(__pyx_t_3);
            __pyx_t_7 = __pyx_t_3;
        }
        __Pyx_DECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        __Pyx_DECREF(__pyx_t_1);
        __pyx_t_1 = 0;

        /* "pyemd/emd.pyx":210
         *     if range is None:
         *         range = (min(np.min(first_array), np.min(second_array)),
         *                  max(np.max(first_array), np.max(second_array)))             # <<<<<<<<<<<<<<
         *     # Get bin edges using both arrays
         *     bins = get_bins(np.concatenate([first_array, second_array]),
         */
        __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_np);
        if (unlikely(!__pyx_t_3))
            __PYX_ERR(0, 210, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_max);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 210, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        __pyx_t_3 = NULL;
        __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
        if (unlikely(PyMethod_Check(__pyx_t_2)))
        {
            __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
            if (likely(__pyx_t_3))
            {
                PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_2);
                __Pyx_INCREF(__pyx_t_3);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_2, function);
                __pyx_t_4 = 1;
            }
        }
#endif
        {
            PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_second_array};
            __pyx_t_1 = __Pyx_PyObject_FastCall(__pyx_t_2, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
            __Pyx_XDECREF(__pyx_t_3);
            __pyx_t_3 = 0;
            if (unlikely(!__pyx_t_1))
                __PYX_ERR(0, 210, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_2);
            __pyx_t_2 = 0;
        }
        __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_np);
        if (unlikely(!__pyx_t_3))
            __PYX_ERR(0, 210, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_max);
        if (unlikely(!__pyx_t_8))
            __PYX_ERR(0, 210, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        __pyx_t_3 = NULL;
        __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
        if (unlikely(PyMethod_Check(__pyx_t_8)))
        {
            __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_8);
            if (likely(__pyx_t_3))
            {
                PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_8);
                __Pyx_INCREF(__pyx_t_3);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_8, function);
                __pyx_t_4 = 1;
            }
        }
#endif
        {
            PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_v_first_array};
            __pyx_t_2 = __Pyx_PyObject_FastCall(__pyx_t_8, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
            __Pyx_XDECREF(__pyx_t_3);
            __pyx_t_3 = 0;
            if (unlikely(!__pyx_t_2))
                __PYX_ERR(0, 210, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_8);
            __pyx_t_8 = 0;
        }
        __pyx_t_3 = PyObject_RichCompare(__pyx_t_1, __pyx_t_2, Py_GT);
        __Pyx_XGOTREF(__pyx_t_3);
        if (unlikely(!__pyx_t_3))
            __PYX_ERR(0, 210, __pyx_L1_error)
        __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_3);
        if (unlikely((__pyx_t_6 < 0)))
            __PYX_ERR(0, 210, __pyx_L1_error)
        __Pyx_DECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        if (__pyx_t_6)
        {
            __Pyx_INCREF(__pyx_t_1);
            __pyx_t_8 = __pyx_t_1;
        }
        else
        {
            __Pyx_INCREF(__pyx_t_2);
            __pyx_t_8 = __pyx_t_2;
        }
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_1);
        __pyx_t_1 = 0;

        /* "pyemd/emd.pyx":209
         *     # Get the default range
         *     if range is None:
         *         range = (min(np.min(first_array), np.min(second_array)),             # <<<<<<<<<<<<<<
         *                  max(np.max(first_array), np.max(second_array)))
         *     # Get bin edges using both arrays
         */
        __pyx_t_1 = PyTuple_New(2);
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 209, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_GIVEREF(__pyx_t_7);
        if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_7))
            __PYX_ERR(0, 209, __pyx_L1_error);
        __Pyx_INCREF(__pyx_t_8);
        __Pyx_GIVEREF(__pyx_t_8);
        if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_8))
            __PYX_ERR(0, 209, __pyx_L1_error);
        __Pyx_DECREF(__pyx_t_7);
        __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_8);
        __pyx_t_8 = 0;
        __Pyx_DECREF_SET(__pyx_v_range, __pyx_t_1);
        __pyx_t_1 = 0;

        /* "pyemd/emd.pyx":208
         *         raise ValueError('Arrays of samples cannot be empty.')
         *     # Get the default range
         *     if range is None:             # <<<<<<<<<<<<<<
         *         range = (min(np.min(first_array), np.min(second_array)),
         *                  max(np.max(first_array), np.max(second_array)))
         */
    }

    /* "pyemd/emd.pyx":212
     *                  max(np.max(first_array), np.max(second_array)))
     *     # Get bin edges using both arrays
     *     bins = get_bins(np.concatenate([first_array, second_array]),             # <<<<<<<<<<<<<<
     *                     range=range,
     *                     bins=bins)
     */
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_get_bins);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 212, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_np);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 212, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_concatenate);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 212, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_7);
    __pyx_t_7 = 0;
    __pyx_t_7 = PyList_New(2);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 212, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_INCREF(__pyx_v_first_array);
    __Pyx_GIVEREF(__pyx_v_first_array);
    if (__Pyx_PyList_SET_ITEM(__pyx_t_7, 0, __pyx_v_first_array))
        __PYX_ERR(0, 212, __pyx_L1_error);
    __Pyx_INCREF(__pyx_v_second_array);
    __Pyx_GIVEREF(__pyx_v_second_array);
    if (__Pyx_PyList_SET_ITEM(__pyx_t_7, 1, __pyx_v_second_array))
        __PYX_ERR(0, 212, __pyx_L1_error);
    __pyx_t_3 = NULL;
    __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_2)))
    {
        __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
        if (likely(__pyx_t_3))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
            __pyx_t_4 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[2] = {__pyx_t_3, __pyx_t_7};
        __pyx_t_8 = __Pyx_PyObject_FastCall(__pyx_t_2, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
        __Pyx_XDECREF(__pyx_t_3);
        __pyx_t_3 = 0;
        __Pyx_DECREF(__pyx_t_7);
        __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_8))
            __PYX_ERR(0, 212, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
    }
    __pyx_t_2 = PyTuple_New(1);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 212, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_GIVEREF(__pyx_t_8);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_8))
        __PYX_ERR(0, 212, __pyx_L1_error);
    __pyx_t_8 = 0;

    /* "pyemd/emd.pyx":213
     *     # Get bin edges using both arrays
     *     bins = get_bins(np.concatenate([first_array, second_array]),
     *                     range=range,             # <<<<<<<<<<<<<<
     *                     bins=bins)
     *     # Compute histograms
     */
    __pyx_t_8 = __Pyx_PyDict_NewPresized(2);
    if (unlikely(!__pyx_t_8))
        __PYX_ERR(0, 213, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    if (PyDict_SetItem(__pyx_t_8, __pyx_n_s_range, __pyx_v_range) < 0)
        __PYX_ERR(0, 213, __pyx_L1_error)

    /* "pyemd/emd.pyx":214
     *     bins = get_bins(np.concatenate([first_array, second_array]),
     *                     range=range,
     *                     bins=bins)             # <<<<<<<<<<<<<<
     *     # Compute histograms
     *     first_histogram, bin_edges = np.histogram(first_array,
     */
    if (PyDict_SetItem(__pyx_t_8, __pyx_n_s_bins, __pyx_v_bins) < 0)
        __PYX_ERR(0, 213, __pyx_L1_error)

    /* "pyemd/emd.pyx":212
     *                  max(np.max(first_array), np.max(second_array)))
     *     # Get bin edges using both arrays
     *     bins = get_bins(np.concatenate([first_array, second_array]),             # <<<<<<<<<<<<<<
     *                     range=range,
     *                     bins=bins)
     */
    __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_2, __pyx_t_8);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 212, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_8);
    __pyx_t_8 = 0;
    __Pyx_DECREF_SET(__pyx_v_bins, __pyx_t_7);
    __pyx_t_7 = 0;

    /* "pyemd/emd.pyx":216
     *                     bins=bins)
     *     # Compute histograms
     *     first_histogram, bin_edges = np.histogram(first_array,             # <<<<<<<<<<<<<<
     *                                               range=range,
     *                                               bins=bins)
     */
    __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_np);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 216, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_histogram);
    if (unlikely(!__pyx_t_8))
        __PYX_ERR(0, 216, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_7);
    __pyx_t_7 = 0;
    __pyx_t_7 = PyTuple_New(1);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 216, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_INCREF(__pyx_v_first_array);
    __Pyx_GIVEREF(__pyx_v_first_array);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_v_first_array))
        __PYX_ERR(0, 216, __pyx_L1_error);

    /* "pyemd/emd.pyx":217
     *     # Compute histograms
     *     first_histogram, bin_edges = np.histogram(first_array,
     *                                               range=range,             # <<<<<<<<<<<<<<
     *                                               bins=bins)
     *     second_histogram, _ = np.histogram(second_array,
     */
    __pyx_t_2 = __Pyx_PyDict_NewPresized(2);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 217, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_range, __pyx_v_range) < 0)
        __PYX_ERR(0, 217, __pyx_L1_error)

    /* "pyemd/emd.pyx":218
     *     first_histogram, bin_edges = np.histogram(first_array,
     *                                               range=range,
     *                                               bins=bins)             # <<<<<<<<<<<<<<
     *     second_histogram, _ = np.histogram(second_array,
     *                                        range=range,
     */
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_bins, __pyx_v_bins) < 0)
        __PYX_ERR(0, 217, __pyx_L1_error)

    /* "pyemd/emd.pyx":216
     *                     bins=bins)
     *     # Compute histograms
     *     first_histogram, bin_edges = np.histogram(first_array,             # <<<<<<<<<<<<<<
     *                                               range=range,
     *                                               bins=bins)
     */
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_8, __pyx_t_7, __pyx_t_2);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 216, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_8);
    __pyx_t_8 = 0;
    __Pyx_DECREF(__pyx_t_7);
    __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    if ((likely(PyTuple_CheckExact(__pyx_t_1))) || (PyList_CheckExact(__pyx_t_1)))
    {
        PyObject *sequence = __pyx_t_1;
        Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
        if (unlikely(size != 2))
        {
            if (size > 2)
                __Pyx_RaiseTooManyValuesError(2);
            else if (size >= 0)
                __Pyx_RaiseNeedMoreValuesError(size);
            __PYX_ERR(0, 216, __pyx_L1_error)
        }
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        if (likely(PyTuple_CheckExact(sequence)))
        {
            __pyx_t_2 = PyTuple_GET_ITEM(sequence, 0);
            __pyx_t_7 = PyTuple_GET_ITEM(sequence, 1);
        }
        else
        {
            __pyx_t_2 = PyList_GET_ITEM(sequence, 0);
            __pyx_t_7 = PyList_GET_ITEM(sequence, 1);
        }
        __Pyx_INCREF(__pyx_t_2);
        __Pyx_INCREF(__pyx_t_7);
#else
        __pyx_t_2 = PySequence_ITEM(sequence, 0);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 216, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_7 = PySequence_ITEM(sequence, 1);
        if (unlikely(!__pyx_t_7))
            __PYX_ERR(0, 216, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_7);
#endif
        __Pyx_DECREF(__pyx_t_1);
        __pyx_t_1 = 0;
    }
    else
    {
        Py_ssize_t index = -1;
        __pyx_t_8 = PyObject_GetIter(__pyx_t_1);
        if (unlikely(!__pyx_t_8))
            __PYX_ERR(0, 216, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_1);
        __pyx_t_1 = 0;
        __pyx_t_9 = __Pyx_PyObject_GetIterNextFunc(__pyx_t_8);
        index = 0;
        __pyx_t_2 = __pyx_t_9(__pyx_t_8);
        if (unlikely(!__pyx_t_2))
            goto __pyx_L7_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_2);
        index = 1;
        __pyx_t_7 = __pyx_t_9(__pyx_t_8);
        if (unlikely(!__pyx_t_7))
            goto __pyx_L7_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_7);
        if (__Pyx_IternextUnpackEndCheck(__pyx_t_9(__pyx_t_8), 2) < 0)
            __PYX_ERR(0, 216, __pyx_L1_error)
        __pyx_t_9 = NULL;
        __Pyx_DECREF(__pyx_t_8);
        __pyx_t_8 = 0;
        goto __pyx_L8_unpacking_done;
    __pyx_L7_unpacking_failed:;
        __Pyx_DECREF(__pyx_t_8);
        __pyx_t_8 = 0;
        __pyx_t_9 = NULL;
        if (__Pyx_IterFinish() == 0)
            __Pyx_RaiseNeedMoreValuesError(index);
        __PYX_ERR(0, 216, __pyx_L1_error)
    __pyx_L8_unpacking_done:;
    }
    __pyx_v_first_histogram = __pyx_t_2;
    __pyx_t_2 = 0;
    __pyx_v_bin_edges = __pyx_t_7;
    __pyx_t_7 = 0;

    /* "pyemd/emd.pyx":219
     *                                               range=range,
     *                                               bins=bins)
     *     second_histogram, _ = np.histogram(second_array,             # <<<<<<<<<<<<<<
     *                                        range=range,
     *                                        bins=bins)
     */
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_np);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 219, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_histogram);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 219, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __pyx_t_1 = PyTuple_New(1);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 219, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_INCREF(__pyx_v_second_array);
    __Pyx_GIVEREF(__pyx_v_second_array);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_v_second_array))
        __PYX_ERR(0, 219, __pyx_L1_error);

    /* "pyemd/emd.pyx":220
     *                                               bins=bins)
     *     second_histogram, _ = np.histogram(second_array,
     *                                        range=range,             # <<<<<<<<<<<<<<
     *                                        bins=bins)
     *     # Cast to C++ long
     */
    __pyx_t_2 = __Pyx_PyDict_NewPresized(2);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 220, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_range, __pyx_v_range) < 0)
        __PYX_ERR(0, 220, __pyx_L1_error)

    /* "pyemd/emd.pyx":221
     *     second_histogram, _ = np.histogram(second_array,
     *                                        range=range,
     *                                        bins=bins)             # <<<<<<<<<<<<<<
     *     # Cast to C++ long
     *     first_histogram = first_histogram.astype(np.float64)
     */
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_bins, __pyx_v_bins) < 0)
        __PYX_ERR(0, 220, __pyx_L1_error)

    /* "pyemd/emd.pyx":219
     *                                               range=range,
     *                                               bins=bins)
     *     second_histogram, _ = np.histogram(second_array,             # <<<<<<<<<<<<<<
     *                                        range=range,
     *                                        bins=bins)
     */
    __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_1, __pyx_t_2);
    if (unlikely(!__pyx_t_8))
        __PYX_ERR(0, 219, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_7);
    __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    if ((likely(PyTuple_CheckExact(__pyx_t_8))) || (PyList_CheckExact(__pyx_t_8)))
    {
        PyObject *sequence = __pyx_t_8;
        Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
        if (unlikely(size != 2))
        {
            if (size > 2)
                __Pyx_RaiseTooManyValuesError(2);
            else if (size >= 0)
                __Pyx_RaiseNeedMoreValuesError(size);
            __PYX_ERR(0, 219, __pyx_L1_error)
        }
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        if (likely(PyTuple_CheckExact(sequence)))
        {
            __pyx_t_2 = PyTuple_GET_ITEM(sequence, 0);
            __pyx_t_1 = PyTuple_GET_ITEM(sequence, 1);
        }
        else
        {
            __pyx_t_2 = PyList_GET_ITEM(sequence, 0);
            __pyx_t_1 = PyList_GET_ITEM(sequence, 1);
        }
        __Pyx_INCREF(__pyx_t_2);
        __Pyx_INCREF(__pyx_t_1);
#else
        __pyx_t_2 = PySequence_ITEM(sequence, 0);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 219, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_1 = PySequence_ITEM(sequence, 1);
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 219, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
#endif
        __Pyx_DECREF(__pyx_t_8);
        __pyx_t_8 = 0;
    }
    else
    {
        Py_ssize_t index = -1;
        __pyx_t_7 = PyObject_GetIter(__pyx_t_8);
        if (unlikely(!__pyx_t_7))
            __PYX_ERR(0, 219, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_8);
        __pyx_t_8 = 0;
        __pyx_t_9 = __Pyx_PyObject_GetIterNextFunc(__pyx_t_7);
        index = 0;
        __pyx_t_2 = __pyx_t_9(__pyx_t_7);
        if (unlikely(!__pyx_t_2))
            goto __pyx_L9_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_2);
        index = 1;
        __pyx_t_1 = __pyx_t_9(__pyx_t_7);
        if (unlikely(!__pyx_t_1))
            goto __pyx_L9_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_1);
        if (__Pyx_IternextUnpackEndCheck(__pyx_t_9(__pyx_t_7), 2) < 0)
            __PYX_ERR(0, 219, __pyx_L1_error)
        __pyx_t_9 = NULL;
        __Pyx_DECREF(__pyx_t_7);
        __pyx_t_7 = 0;
        goto __pyx_L10_unpacking_done;
    __pyx_L9_unpacking_failed:;
        __Pyx_DECREF(__pyx_t_7);
        __pyx_t_7 = 0;
        __pyx_t_9 = NULL;
        if (__Pyx_IterFinish() == 0)
            __Pyx_RaiseNeedMoreValuesError(index);
        __PYX_ERR(0, 219, __pyx_L1_error)
    __pyx_L10_unpacking_done:;
    }
    __pyx_v_second_histogram = __pyx_t_2;
    __pyx_t_2 = 0;
    __pyx_v__ = __pyx_t_1;
    __pyx_t_1 = 0;

    /* "pyemd/emd.pyx":223
     *                                        bins=bins)
     *     # Cast to C++ long
     *     first_histogram = first_histogram.astype(np.float64)             # <<<<<<<<<<<<<<
     *     second_histogram = second_histogram.astype(np.float64)
     *     # Normalize histograms to represent fraction of dataset in each bin
     */
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_first_histogram, __pyx_n_s_astype);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 223, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_np);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 223, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_float64);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 223, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_2 = NULL;
    __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
    if (likely(PyMethod_Check(__pyx_t_1)))
    {
        __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
        if (likely(__pyx_t_2))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_1);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_1, function);
            __pyx_t_4 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[2] = {__pyx_t_2, __pyx_t_7};
        __pyx_t_8 = __Pyx_PyObject_FastCall(__pyx_t_1, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
        __Pyx_XDECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_7);
        __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_8))
            __PYX_ERR(0, 223, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_1);
        __pyx_t_1 = 0;
    }
    __Pyx_DECREF_SET(__pyx_v_first_histogram, __pyx_t_8);
    __pyx_t_8 = 0;

    /* "pyemd/emd.pyx":224
     *     # Cast to C++ long
     *     first_histogram = first_histogram.astype(np.float64)
     *     second_histogram = second_histogram.astype(np.float64)             # <<<<<<<<<<<<<<
     *     # Normalize histograms to represent fraction of dataset in each bin
     *     if normalized:
     */
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_second_histogram, __pyx_n_s_astype);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 224, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_np);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 224, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_float64);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 224, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_7);
    __pyx_t_7 = 0;
    __pyx_t_7 = NULL;
    __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
    if (likely(PyMethod_Check(__pyx_t_1)))
    {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_1);
        if (likely(__pyx_t_7))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_1);
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_1, function);
            __pyx_t_4 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[2] = {__pyx_t_7, __pyx_t_2};
        __pyx_t_8 = __Pyx_PyObject_FastCall(__pyx_t_1, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
        __Pyx_XDECREF(__pyx_t_7);
        __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_8))
            __PYX_ERR(0, 224, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_1);
        __pyx_t_1 = 0;
    }
    __Pyx_DECREF_SET(__pyx_v_second_histogram, __pyx_t_8);
    __pyx_t_8 = 0;

    /* "pyemd/emd.pyx":226
     *     second_histogram = second_histogram.astype(np.float64)
     *     # Normalize histograms to represent fraction of dataset in each bin
     *     if normalized:             # <<<<<<<<<<<<<<
     *         first_histogram = first_histogram / np.sum(first_histogram)
     *         second_histogram = second_histogram / np.sum(second_histogram)
     */
    __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_v_normalized);
    if (unlikely((__pyx_t_6 < 0)))
        __PYX_ERR(0, 226, __pyx_L1_error)
    if (__pyx_t_6)
    {

        /* "pyemd/emd.pyx":227
         *     # Normalize histograms to represent fraction of dataset in each bin
         *     if normalized:
         *         first_histogram = first_histogram / np.sum(first_histogram)             # <<<<<<<<<<<<<<
         *         second_histogram = second_histogram / np.sum(second_histogram)
         *     # Compute the distance matrix between the center of each bin
         */
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_np);
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 227, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_sum);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 227, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_1);
        __pyx_t_1 = 0;
        __pyx_t_1 = NULL;
        __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
        if (unlikely(PyMethod_Check(__pyx_t_2)))
        {
            __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
            if (likely(__pyx_t_1))
            {
                PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_2);
                __Pyx_INCREF(__pyx_t_1);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_2, function);
                __pyx_t_4 = 1;
            }
        }
#endif
        {
            PyObject *__pyx_callargs[2] = {__pyx_t_1, __pyx_v_first_histogram};
            __pyx_t_8 = __Pyx_PyObject_FastCall(__pyx_t_2, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
            __Pyx_XDECREF(__pyx_t_1);
            __pyx_t_1 = 0;
            if (unlikely(!__pyx_t_8))
                __PYX_ERR(0, 227, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_8);
            __Pyx_DECREF(__pyx_t_2);
            __pyx_t_2 = 0;
        }
        __pyx_t_2 = __Pyx_PyNumber_Divide(__pyx_v_first_histogram, __pyx_t_8);
        if (unlikely(!__pyx_t_2))
            __PYX_ERR(0, 227, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_8);
        __pyx_t_8 = 0;
        __Pyx_DECREF_SET(__pyx_v_first_histogram, __pyx_t_2);
        __pyx_t_2 = 0;

        /* "pyemd/emd.pyx":228
         *     if normalized:
         *         first_histogram = first_histogram / np.sum(first_histogram)
         *         second_histogram = second_histogram / np.sum(second_histogram)             # <<<<<<<<<<<<<<
         *     # Compute the distance matrix between the center of each bin
         *     bin_locations = np.mean([bin_edges[:-1], bin_edges[1:]], axis=0)
         */
        __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_np);
        if (unlikely(!__pyx_t_8))
            __PYX_ERR(0, 228, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_8);
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_sum);
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 228, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_8);
        __pyx_t_8 = 0;
        __pyx_t_8 = NULL;
        __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
        if (unlikely(PyMethod_Check(__pyx_t_1)))
        {
            __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_1);
            if (likely(__pyx_t_8))
            {
                PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_1);
                __Pyx_INCREF(__pyx_t_8);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_1, function);
                __pyx_t_4 = 1;
            }
        }
#endif
        {
            PyObject *__pyx_callargs[2] = {__pyx_t_8, __pyx_v_second_histogram};
            __pyx_t_2 = __Pyx_PyObject_FastCall(__pyx_t_1, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
            __Pyx_XDECREF(__pyx_t_8);
            __pyx_t_8 = 0;
            if (unlikely(!__pyx_t_2))
                __PYX_ERR(0, 228, __pyx_L1_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_1);
            __pyx_t_1 = 0;
        }
        __pyx_t_1 = __Pyx_PyNumber_Divide(__pyx_v_second_histogram, __pyx_t_2);
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 228, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2);
        __pyx_t_2 = 0;
        __Pyx_DECREF_SET(__pyx_v_second_histogram, __pyx_t_1);
        __pyx_t_1 = 0;

        /* "pyemd/emd.pyx":226
         *     second_histogram = second_histogram.astype(np.float64)
         *     # Normalize histograms to represent fraction of dataset in each bin
         *     if normalized:             # <<<<<<<<<<<<<<
         *         first_histogram = first_histogram / np.sum(first_histogram)
         *         second_histogram = second_histogram / np.sum(second_histogram)
         */
    }

    /* "pyemd/emd.pyx":230
     *         second_histogram = second_histogram / np.sum(second_histogram)
     *     # Compute the distance matrix between the center of each bin
     *     bin_locations = np.mean([bin_edges[:-1], bin_edges[1:]], axis=0)             # <<<<<<<<<<<<<<
     *     if distance == 'euclidean':
     *         distance = euclidean_pairwise_distance_matrix
     */
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_np);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_mean);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyObject_GetSlice(__pyx_v_bin_edges, 0, -1L, NULL, NULL, &__pyx_slice__6, 0, 1, 1);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_8 = __Pyx_PyObject_GetSlice(__pyx_v_bin_edges, 1, 0, NULL, NULL, &__pyx_slice__7, 1, 0, 1);
    if (unlikely(!__pyx_t_8))
        __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_7 = PyList_New(2);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_GIVEREF(__pyx_t_1);
    if (__Pyx_PyList_SET_ITEM(__pyx_t_7, 0, __pyx_t_1))
        __PYX_ERR(0, 230, __pyx_L1_error);
    __Pyx_GIVEREF(__pyx_t_8);
    if (__Pyx_PyList_SET_ITEM(__pyx_t_7, 1, __pyx_t_8))
        __PYX_ERR(0, 230, __pyx_L1_error);
    __pyx_t_1 = 0;
    __pyx_t_8 = 0;
    __pyx_t_8 = PyTuple_New(1);
    if (unlikely(!__pyx_t_8))
        __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_GIVEREF(__pyx_t_7);
    if (__Pyx_PyTuple_SET_ITEM(__pyx_t_8, 0, __pyx_t_7))
        __PYX_ERR(0, 230, __pyx_L1_error);
    __pyx_t_7 = 0;
    __pyx_t_7 = __Pyx_PyDict_NewPresized(1);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_axis, __pyx_int_0) < 0)
        __PYX_ERR(0, 230, __pyx_L1_error)
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_8, __pyx_t_7);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_8);
    __pyx_t_8 = 0;
    __Pyx_DECREF(__pyx_t_7);
    __pyx_t_7 = 0;
    __pyx_v_bin_locations = __pyx_t_1;
    __pyx_t_1 = 0;

    /* "pyemd/emd.pyx":231
     *     # Compute the distance matrix between the center of each bin
     *     bin_locations = np.mean([bin_edges[:-1], bin_edges[1:]], axis=0)
     *     if distance == 'euclidean':             # <<<<<<<<<<<<<<
     *         distance = euclidean_pairwise_distance_matrix
     *     distance_matrix = distance(bin_locations)
     */
    __pyx_t_6 = (__Pyx_PyUnicode_Equals(__pyx_v_distance, __pyx_n_u_euclidean, Py_EQ));
    if (unlikely((__pyx_t_6 < 0)))
        __PYX_ERR(0, 231, __pyx_L1_error)
    if (__pyx_t_6)
    {

        /* "pyemd/emd.pyx":232
         *     bin_locations = np.mean([bin_edges[:-1], bin_edges[1:]], axis=0)
         *     if distance == 'euclidean':
         *         distance = euclidean_pairwise_distance_matrix             # <<<<<<<<<<<<<<
         *     distance_matrix = distance(bin_locations)
         *     # Validate distance matrix
         */
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_euclidean_pairwise_distance_matr);
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 232, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF_SET(__pyx_v_distance, __pyx_t_1);
        __pyx_t_1 = 0;

        /* "pyemd/emd.pyx":231
         *     # Compute the distance matrix between the center of each bin
         *     bin_locations = np.mean([bin_edges[:-1], bin_edges[1:]], axis=0)
         *     if distance == 'euclidean':             # <<<<<<<<<<<<<<
         *         distance = euclidean_pairwise_distance_matrix
         *     distance_matrix = distance(bin_locations)
         */
    }

    /* "pyemd/emd.pyx":233
     *     if distance == 'euclidean':
     *         distance = euclidean_pairwise_distance_matrix
     *     distance_matrix = distance(bin_locations)             # <<<<<<<<<<<<<<
     *     # Validate distance matrix
     *     if len(distance_matrix) != len(distance_matrix[0]):
     */
    __Pyx_INCREF(__pyx_v_distance);
    __pyx_t_7 = __pyx_v_distance;
    __pyx_t_8 = NULL;
    __pyx_t_4 = 0;
#if CYTHON_UNPACK_METHODS
    if (unlikely(PyMethod_Check(__pyx_t_7)))
    {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_7);
        if (likely(__pyx_t_8))
        {
            PyObject *function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
            __pyx_t_4 = 1;
        }
    }
#endif
    {
        PyObject *__pyx_callargs[2] = {__pyx_t_8, __pyx_v_bin_locations};
        __pyx_t_1 = __Pyx_PyObject_FastCall(__pyx_t_7, __pyx_callargs + 1 - __pyx_t_4, 1 + __pyx_t_4);
        __Pyx_XDECREF(__pyx_t_8);
        __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 233, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_7);
        __pyx_t_7 = 0;
    }
    __pyx_v_distance_matrix = __pyx_t_1;
    __pyx_t_1 = 0;

    /* "pyemd/emd.pyx":235
     *     distance_matrix = distance(bin_locations)
     *     # Validate distance matrix
     *     if len(distance_matrix) != len(distance_matrix[0]):             # <<<<<<<<<<<<<<
     *         raise ValueError(
     *             'Distance matrix must be square; check your `distance` function.')
     */
    __pyx_t_10 = PyObject_Length(__pyx_v_distance_matrix);
    if (unlikely(__pyx_t_10 == ((Py_ssize_t)-1)))
        __PYX_ERR(0, 235, __pyx_L1_error)
    __pyx_t_1 = __Pyx_GetItemInt(__pyx_v_distance_matrix, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 235, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_11 = PyObject_Length(__pyx_t_1);
    if (unlikely(__pyx_t_11 == ((Py_ssize_t)-1)))
        __PYX_ERR(0, 235, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __pyx_t_6 = (__pyx_t_10 != __pyx_t_11);
    if (unlikely(__pyx_t_6))
    {

        /* "pyemd/emd.pyx":236
         *     # Validate distance matrix
         *     if len(distance_matrix) != len(distance_matrix[0]):
         *         raise ValueError(             # <<<<<<<<<<<<<<
         *             'Distance matrix must be square; check your `distance` function.')
         *     if (first_histogram.shape[0] > len(distance_matrix) or
         */
        __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_ValueError, __pyx_tuple__8, NULL);
        if (unlikely(!__pyx_t_1))
            __PYX_ERR(0, 236, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_Raise(__pyx_t_1, 0, 0, 0);
        __Pyx_DECREF(__pyx_t_1);
        __pyx_t_1 = 0;
        __PYX_ERR(0, 236, __pyx_L1_error)

        /* "pyemd/emd.pyx":235
         *     distance_matrix = distance(bin_locations)
         *     # Validate distance matrix
         *     if len(distance_matrix) != len(distance_matrix[0]):             # <<<<<<<<<<<<<<
         *         raise ValueError(
         *             'Distance matrix must be square; check your `distance` function.')
         */
    }

    /* "pyemd/emd.pyx":238
     *         raise ValueError(
     *             'Distance matrix must be square; check your `distance` function.')
     *     if (first_histogram.shape[0] > len(distance_matrix) or             # <<<<<<<<<<<<<<
     *         second_histogram.shape[0] > len(distance_matrix)):
     *         raise ValueError(
     */
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_first_histogram, __pyx_n_s_shape);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 238, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_7 = __Pyx_GetItemInt(__pyx_t_1, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 238, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __pyx_t_11 = PyObject_Length(__pyx_v_distance_matrix);
    if (unlikely(__pyx_t_11 == ((Py_ssize_t)-1)))
        __PYX_ERR(0, 238, __pyx_L1_error)
    __pyx_t_1 = PyInt_FromSsize_t(__pyx_t_11);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 238, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_8 = PyObject_RichCompare(__pyx_t_7, __pyx_t_1, Py_GT);
    __Pyx_XGOTREF(__pyx_t_8);
    if (unlikely(!__pyx_t_8))
        __PYX_ERR(0, 238, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_7);
    __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_8);
    if (unlikely((__pyx_t_5 < 0)))
        __PYX_ERR(0, 238, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_8);
    __pyx_t_8 = 0;
    if (!__pyx_t_5)
    {
    }
    else
    {
        __pyx_t_6 = __pyx_t_5;
        goto __pyx_L15_bool_binop_done;
    }

    /* "pyemd/emd.pyx":239
     *             'Distance matrix must be square; check your `distance` function.')
     *     if (first_histogram.shape[0] > len(distance_matrix) or
     *         second_histogram.shape[0] > len(distance_matrix)):             # <<<<<<<<<<<<<<
     *         raise ValueError(
     *             'Distance matrix must have at least as many rows/columns as there '
     */
    __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_second_histogram, __pyx_n_s_shape);
    if (unlikely(!__pyx_t_8))
        __PYX_ERR(0, 239, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_1 = __Pyx_GetItemInt(__pyx_t_8, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 239, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_8);
    __pyx_t_8 = 0;
    __pyx_t_11 = PyObject_Length(__pyx_v_distance_matrix);
    if (unlikely(__pyx_t_11 == ((Py_ssize_t)-1)))
        __PYX_ERR(0, 239, __pyx_L1_error)
    __pyx_t_8 = PyInt_FromSsize_t(__pyx_t_11);
    if (unlikely(!__pyx_t_8))
        __PYX_ERR(0, 239, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_7 = PyObject_RichCompare(__pyx_t_1, __pyx_t_8, Py_GT);
    __Pyx_XGOTREF(__pyx_t_7);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 239, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_8);
    __pyx_t_8 = 0;
    __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_7);
    if (unlikely((__pyx_t_5 < 0)))
        __PYX_ERR(0, 239, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_7);
    __pyx_t_7 = 0;
    __pyx_t_6 = __pyx_t_5;
__pyx_L15_bool_binop_done:;

    /* "pyemd/emd.pyx":238
     *         raise ValueError(
     *             'Distance matrix must be square; check your `distance` function.')
     *     if (first_histogram.shape[0] > len(distance_matrix) or             # <<<<<<<<<<<<<<
     *         second_histogram.shape[0] > len(distance_matrix)):
     *         raise ValueError(
     */
    if (unlikely(__pyx_t_6))
    {

        /* "pyemd/emd.pyx":240
         *     if (first_histogram.shape[0] > len(distance_matrix) or
         *         second_histogram.shape[0] > len(distance_matrix)):
         *         raise ValueError(             # <<<<<<<<<<<<<<
         *             'Distance matrix must have at least as many rows/columns as there '
         *             'are bins in the histograms; check your `distance` function.')
         */
        __pyx_t_7 = __Pyx_PyObject_Call(__pyx_builtin_ValueError, __pyx_tuple__9, NULL);
        if (unlikely(!__pyx_t_7))
            __PYX_ERR(0, 240, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_Raise(__pyx_t_7, 0, 0, 0);
        __Pyx_DECREF(__pyx_t_7);
        __pyx_t_7 = 0;
        __PYX_ERR(0, 240, __pyx_L1_error)

        /* "pyemd/emd.pyx":238
         *         raise ValueError(
         *             'Distance matrix must be square; check your `distance` function.')
         *     if (first_histogram.shape[0] > len(distance_matrix) or             # <<<<<<<<<<<<<<
         *         second_histogram.shape[0] > len(distance_matrix)):
         *         raise ValueError(
         */
    }

    /* "pyemd/emd.pyx":245
     *     # Return the EMD (no need to call the wrapper function, since this function
     *     # does its own validation, so we call the exposed C++ function directly)
     *     return emd_hat_gd_metric_double(first_histogram,             # <<<<<<<<<<<<<<
     *                                     second_histogram,
     *                                     distance_matrix,
     */
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_12 = __pyx_convert_vector_from_py_double(__pyx_v_first_histogram);
    if (unlikely(PyErr_Occurred()))
        __PYX_ERR(0, 245, __pyx_L1_error)

    /* "pyemd/emd.pyx":246
     *     # does its own validation, so we call the exposed C++ function directly)
     *     return emd_hat_gd_metric_double(first_histogram,
     *                                     second_histogram,             # <<<<<<<<<<<<<<
     *                                     distance_matrix,
     *                                     extra_mass_penalty)
     */
    __pyx_t_13 = __pyx_convert_vector_from_py_double(__pyx_v_second_histogram);
    if (unlikely(PyErr_Occurred()))
        __PYX_ERR(0, 246, __pyx_L1_error)

    /* "pyemd/emd.pyx":247
     *     return emd_hat_gd_metric_double(first_histogram,
     *                                     second_histogram,
     *                                     distance_matrix,             # <<<<<<<<<<<<<<
     *                                     extra_mass_penalty)
     */
    __pyx_t_14 = __pyx_convert_vector_from_py_std_3a__3a_vector_3c_double_3e___(__pyx_v_distance_matrix);
    if (unlikely(PyErr_Occurred()))
        __PYX_ERR(0, 247, __pyx_L1_error)

    /* "pyemd/emd.pyx":248
     *                                     second_histogram,
     *                                     distance_matrix,
     *                                     extra_mass_penalty)             # <<<<<<<<<<<<<<
     */
    __pyx_t_15 = __pyx_PyFloat_AsDouble(__pyx_v_extra_mass_penalty);
    if (unlikely((__pyx_t_15 == (double)-1) && PyErr_Occurred()))
        __PYX_ERR(0, 248, __pyx_L1_error)

    /* "pyemd/emd.pyx":245
     *     # Return the EMD (no need to call the wrapper function, since this function
     *     # does its own validation, so we call the exposed C++ function directly)
     *     return emd_hat_gd_metric_double(first_histogram,             # <<<<<<<<<<<<<<
     *                                     second_histogram,
     *                                     distance_matrix,
     */
    try
    {
        __pyx_t_16 = emd_hat_gd_metric_double(__PYX_STD_MOVE_IF_SUPPORTED(__pyx_t_12), __PYX_STD_MOVE_IF_SUPPORTED(__pyx_t_13), __PYX_STD_MOVE_IF_SUPPORTED(__pyx_t_14), __pyx_t_15);
    }
    catch (...)
    {
        __Pyx_CppExn2PyErr();
        __PYX_ERR(0, 245, __pyx_L1_error)
    }
    __pyx_t_7 = PyFloat_FromDouble(__pyx_t_16);
    if (unlikely(!__pyx_t_7))
        __PYX_ERR(0, 245, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_r = __pyx_t_7;
    __pyx_t_7 = 0;
    goto __pyx_L0;

/* "pyemd/emd.pyx":154
 *
 *
 * def emd_samples(first_array,             # <<<<<<<<<<<<<<
 *                 second_array,
 *                 extra_mass_penalty=DEFAULT_EXTRA_MASS_PENALTY,
 */

/* function exit code */
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_3);
    __Pyx_XDECREF(__pyx_t_7);
    __Pyx_XDECREF(__pyx_t_8);
    __Pyx_AddTraceback("pyemd.emd.emd_samples", __pyx_clineno, __pyx_lineno, __pyx_filename);
    __pyx_r = NULL;
__pyx_L0:;
    __Pyx_XDECREF(__pyx_v_first_histogram);
    __Pyx_XDECREF(__pyx_v_bin_edges);
    __Pyx_XDECREF(__pyx_v_second_histogram);
    __Pyx_XDECREF(__pyx_v__);
    __Pyx_XDECREF(__pyx_v_bin_locations);
    __Pyx_XDECREF(__pyx_v_distance_matrix);
    __Pyx_XDECREF(__pyx_v_first_array);
    __Pyx_XDECREF(__pyx_v_second_array);
    __Pyx_XDECREF(__pyx_v_distance);
    __Pyx_XDECREF(__pyx_v_bins);
    __Pyx_XDECREF(__pyx_v_range);
    __Pyx_XGIVEREF(__pyx_r);
    __Pyx_RefNannyFinishContext();
    return __pyx_r;
}

static PyMethodDef __pyx_methods[] = {
    {0, 0, 0, 0}};
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
#define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
#define CYTHON_SMALL_CODE __attribute__((cold))
#else
#define CYTHON_SMALL_CODE
#endif
#endif
/* #### Code section: pystring_table ### */

static int __Pyx_CreateStringTabAndInitStrings(void)
{
    __Pyx_StringTabEntry __pyx_string_tab[] = {
        {&__pyx_kp_u_1_15_0, __pyx_k_1_15_0, sizeof(__pyx_k_1_15_0), 0, 1, 0, 0},
        {&__pyx_kp_u_Arrays_of_samples_cannot_be_empt, __pyx_k_Arrays_of_samples_cannot_be_empt, sizeof(__pyx_k_Arrays_of_samples_cannot_be_empt), 0, 1, 0, 0},
        {&__pyx_n_s_DEFAULT_EXTRA_MASS_PENALTY, __pyx_k_DEFAULT_EXTRA_MASS_PENALTY, sizeof(__pyx_k_DEFAULT_EXTRA_MASS_PENALTY), 0, 0, 1, 1},
        {&__pyx_kp_u_Distance_matrix_must_be_square_c, __pyx_k_Distance_matrix_must_be_square_c, sizeof(__pyx_k_Distance_matrix_must_be_square_c), 0, 1, 0, 0},
        {&__pyx_kp_u_Distance_matrix_must_have_at_lea, __pyx_k_Distance_matrix_must_have_at_lea, sizeof(__pyx_k_Distance_matrix_must_have_at_lea), 0, 1, 0, 0},
        {&__pyx_kp_u_Histogram_lengths_cannot_be_grea, __pyx_k_Histogram_lengths_cannot_be_grea, sizeof(__pyx_k_Histogram_lengths_cannot_be_grea), 0, 1, 0, 0},
        {&__pyx_kp_u_Histogram_lengths_must_be_equal, __pyx_k_Histogram_lengths_must_be_equal, sizeof(__pyx_k_Histogram_lengths_must_be_equal), 0, 1, 0, 0},
        {&__pyx_n_s_ImportError, __pyx_k_ImportError, sizeof(__pyx_k_ImportError), 0, 0, 1, 1},
        {&__pyx_n_s_MemoryError, __pyx_k_MemoryError, sizeof(__pyx_k_MemoryError), 0, 0, 1, 1},
        {&__pyx_n_s_ValueError, __pyx_k_ValueError, sizeof(__pyx_k_ValueError), 0, 0, 1, 1},
        {&__pyx_kp_u__10, __pyx_k__10, sizeof(__pyx_k__10), 0, 1, 0, 0},
        {&__pyx_n_s__11, __pyx_k__11, sizeof(__pyx_k__11), 0, 0, 1, 1},
        {&__pyx_n_s__23, __pyx_k__23, sizeof(__pyx_k__23), 0, 0, 1, 1},
        {&__pyx_n_s__26, __pyx_k__26, sizeof(__pyx_k__26), 0, 0, 1, 1},
        {&__pyx_n_s_a, __pyx_k_a, sizeof(__pyx_k_a), 0, 0, 1, 1},
        {&__pyx_n_s_abs, __pyx_k_abs, sizeof(__pyx_k_abs), 0, 0, 1, 1},
        {&__pyx_n_s_array, __pyx_k_array, sizeof(__pyx_k_array), 0, 0, 1, 1},
        {&__pyx_n_s_astype, __pyx_k_astype, sizeof(__pyx_k_astype), 0, 0, 1, 1},
        {&__pyx_n_s_asyncio_coroutines, __pyx_k_asyncio_coroutines, sizeof(__pyx_k_asyncio_coroutines), 0, 0, 1, 1},
        {&__pyx_n_u_auto, __pyx_k_auto, sizeof(__pyx_k_auto), 0, 1, 0, 1},
        {&__pyx_n_s_axis, __pyx_k_axis, sizeof(__pyx_k_axis), 0, 0, 1, 1},
        {&__pyx_n_s_bin_edges, __pyx_k_bin_edges, sizeof(__pyx_k_bin_edges), 0, 0, 1, 1},
        {&__pyx_n_s_bin_locations, __pyx_k_bin_locations, sizeof(__pyx_k_bin_locations), 0, 0, 1, 1},
        {&__pyx_n_s_bins, __pyx_k_bins, sizeof(__pyx_k_bins), 0, 0, 1, 1},
        {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
        {&__pyx_n_s_concatenate, __pyx_k_concatenate, sizeof(__pyx_k_concatenate), 0, 0, 1, 1},
        {&__pyx_n_s_distance, __pyx_k_distance, sizeof(__pyx_k_distance), 0, 0, 1, 1},
        {&__pyx_n_s_distance_matrix, __pyx_k_distance_matrix, sizeof(__pyx_k_distance_matrix), 0, 0, 1, 1},
        {&__pyx_n_s_emd, __pyx_k_emd, sizeof(__pyx_k_emd), 0, 0, 1, 1},
        {&__pyx_n_s_emd_samples, __pyx_k_emd_samples, sizeof(__pyx_k_emd_samples), 0, 0, 1, 1},
        {&__pyx_n_s_emd_with_flow, __pyx_k_emd_with_flow, sizeof(__pyx_k_emd_with_flow), 0, 0, 1, 1},
        {&__pyx_n_u_euclidean, __pyx_k_euclidean, sizeof(__pyx_k_euclidean), 0, 1, 0, 1},
        {&__pyx_n_s_euclidean_pairwise_distance_matr, __pyx_k_euclidean_pairwise_distance_matr, sizeof(__pyx_k_euclidean_pairwise_distance_matr), 0, 0, 1, 1},
        {&__pyx_n_s_extra_mass_penalty, __pyx_k_extra_mass_penalty, sizeof(__pyx_k_extra_mass_penalty), 0, 0, 1, 1},
        {&__pyx_n_s_first_array, __pyx_k_first_array, sizeof(__pyx_k_first_array), 0, 0, 1, 1},
        {&__pyx_n_s_first_histogram, __pyx_k_first_histogram, sizeof(__pyx_k_first_histogram), 0, 0, 1, 1},
        {&__pyx_n_s_float64, __pyx_k_float64, sizeof(__pyx_k_float64), 0, 0, 1, 1},
        {&__pyx_n_s_get_bins, __pyx_k_get_bins, sizeof(__pyx_k_get_bins), 0, 0, 1, 1},
        {&__pyx_n_s_hist, __pyx_k_hist, sizeof(__pyx_k_hist), 0, 0, 1, 1},
        {&__pyx_n_s_histogram, __pyx_k_histogram, sizeof(__pyx_k_histogram), 0, 0, 1, 1},
        {&__pyx_n_s_histogram_bin_edges, __pyx_k_histogram_bin_edges, sizeof(__pyx_k_histogram_bin_edges), 0, 0, 1, 1},
        {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
        {&__pyx_n_s_initializing, __pyx_k_initializing, sizeof(__pyx_k_initializing), 0, 0, 1, 1},
        {&__pyx_n_s_is_coroutine, __pyx_k_is_coroutine, sizeof(__pyx_k_is_coroutine), 0, 0, 1, 1},
        {&__pyx_n_s_items, __pyx_k_items, sizeof(__pyx_k_items), 0, 0, 1, 1},
        {&__pyx_n_s_kwargs, __pyx_k_kwargs, sizeof(__pyx_k_kwargs), 0, 0, 1, 1},
        {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
        {&__pyx_n_s_max, __pyx_k_max, sizeof(__pyx_k_max), 0, 0, 1, 1},
        {&__pyx_n_s_mean, __pyx_k_mean, sizeof(__pyx_k_mean), 0, 0, 1, 1},
        {&__pyx_n_s_min, __pyx_k_min, sizeof(__pyx_k_min), 0, 0, 1, 1},
        {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
        {&__pyx_n_s_normalized, __pyx_k_normalized, sizeof(__pyx_k_normalized), 0, 0, 1, 1},
        {&__pyx_n_s_np, __pyx_k_np, sizeof(__pyx_k_np), 0, 0, 1, 1},
        {&__pyx_n_s_numpy, __pyx_k_numpy, sizeof(__pyx_k_numpy), 0, 0, 1, 1},
        {&__pyx_kp_u_numpy_core_multiarray_failed_to, __pyx_k_numpy_core_multiarray_failed_to, sizeof(__pyx_k_numpy_core_multiarray_failed_to), 0, 1, 0, 0},
        {&__pyx_kp_u_numpy_core_umath_failed_to_impor, __pyx_k_numpy_core_umath_failed_to_impor, sizeof(__pyx_k_numpy_core_umath_failed_to_impor), 0, 1, 0, 0},
        {&__pyx_n_s_parse_version, __pyx_k_parse_version, sizeof(__pyx_k_parse_version), 0, 0, 1, 1},
        {&__pyx_n_s_pkg_resources, __pyx_k_pkg_resources, sizeof(__pyx_k_pkg_resources), 0, 0, 1, 1},
        {&__pyx_n_s_pyemd_emd, __pyx_k_pyemd_emd, sizeof(__pyx_k_pyemd_emd), 0, 0, 1, 1},
        {&__pyx_n_s_range, __pyx_k_range, sizeof(__pyx_k_range), 0, 0, 1, 1},
        {&__pyx_n_s_repeat, __pyx_k_repeat, sizeof(__pyx_k_repeat), 0, 0, 1, 1},
        {&__pyx_n_s_reshape, __pyx_k_reshape, sizeof(__pyx_k_reshape), 0, 0, 1, 1},
        {&__pyx_n_s_second_array, __pyx_k_second_array, sizeof(__pyx_k_second_array), 0, 0, 1, 1},
        {&__pyx_n_s_second_histogram, __pyx_k_second_histogram, sizeof(__pyx_k_second_histogram), 0, 0, 1, 1},
        {&__pyx_n_s_shape, __pyx_k_shape, sizeof(__pyx_k_shape), 0, 0, 1, 1},
        {&__pyx_n_s_size, __pyx_k_size, sizeof(__pyx_k_size), 0, 0, 1, 1},
        {&__pyx_n_s_spec, __pyx_k_spec, sizeof(__pyx_k_spec), 0, 0, 1, 1},
        {&__pyx_kp_s_src_pyemd_emd_pyx, __pyx_k_src_pyemd_emd_pyx, sizeof(__pyx_k_src_pyemd_emd_pyx), 0, 0, 1, 0},
        {&__pyx_n_s_sum, __pyx_k_sum, sizeof(__pyx_k_sum), 0, 0, 1, 1},
        {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
        {&__pyx_n_s_tile, __pyx_k_tile, sizeof(__pyx_k_tile), 0, 0, 1, 1},
        {&__pyx_n_s_validate_emd_input, __pyx_k_validate_emd_input, sizeof(__pyx_k_validate_emd_input), 0, 0, 1, 1},
        {&__pyx_n_s_version, __pyx_k_version, sizeof(__pyx_k_version), 0, 0, 1, 1},
        {&__pyx_n_s_x, __pyx_k_x, sizeof(__pyx_k_x), 0, 0, 1, 1},
        {0, 0, 0, 0, 0, 0, 0}};
    return __Pyx_InitStrings(__pyx_string_tab);
}
/* #### Code section: cached_builtins ### */
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void)
{
    __pyx_builtin_ValueError = __Pyx_GetBuiltinName(__pyx_n_s_ValueError);
    if (!__pyx_builtin_ValueError)
        __PYX_ERR(0, 45, __pyx_L1_error)
    __pyx_builtin_MemoryError = __Pyx_GetBuiltinName(__pyx_n_s_MemoryError);
    if (!__pyx_builtin_MemoryError)
        __PYX_ERR(1, 68, __pyx_L1_error)
    __pyx_builtin_range = __Pyx_GetBuiltinName(__pyx_n_s_range);
    if (!__pyx_builtin_range)
        __PYX_ERR(1, 76, __pyx_L1_error)
    __pyx_builtin_ImportError = __Pyx_GetBuiltinName(__pyx_n_s_ImportError);
    if (!__pyx_builtin_ImportError)
        __PYX_ERR(2, 984, __pyx_L1_error)
    return 0;
__pyx_L1_error:;
    return -1;
}
/* #### Code section: cached_constants ### */

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void)
{
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":984
     *         __pyx_import_array()
     *     except Exception:
     *         raise ImportError("numpy.core.multiarray failed to import")             # <<<<<<<<<<<<<<
     *
     * cdef inline int import_umath() except -1:
     */
    __pyx_tuple_ = PyTuple_Pack(1, __pyx_kp_u_numpy_core_multiarray_failed_to);
    if (unlikely(!__pyx_tuple_))
        __PYX_ERR(2, 984, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple_);
    __Pyx_GIVEREF(__pyx_tuple_);

    /* "../../pip-build-env-jnb8d7ub/overlay/Lib/site-packages/numpy/__init__.cython-30.pxd":990
     *         _import_umath()
     *     except Exception:
     *         raise ImportError("numpy.core.umath failed to import")             # <<<<<<<<<<<<<<
     *
     * cdef inline int import_ufunc() except -1:
     */
    __pyx_tuple__2 = PyTuple_Pack(1, __pyx_kp_u_numpy_core_umath_failed_to_impor);
    if (unlikely(!__pyx_tuple__2))
        __PYX_ERR(2, 990, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__2);
    __Pyx_GIVEREF(__pyx_tuple__2);

    /* "pyemd/emd.pyx":45
     *     if (first_histogram.shape[0] > distance_matrix.shape[0] or
     *         second_histogram.shape[0] > distance_matrix.shape[0]):
     *         raise ValueError('Histogram lengths cannot be greater than the '             # <<<<<<<<<<<<<<
     *                          'number of rows or columns of the distance matrix')
     *     if (first_histogram.shape[0] != second_histogram.shape[0]):
     */
    __pyx_tuple__3 = PyTuple_Pack(1, __pyx_kp_u_Histogram_lengths_cannot_be_grea);
    if (unlikely(!__pyx_tuple__3))
        __PYX_ERR(0, 45, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__3);
    __Pyx_GIVEREF(__pyx_tuple__3);

    /* "pyemd/emd.pyx":48
     *                          'number of rows or columns of the distance matrix')
     *     if (first_histogram.shape[0] != second_histogram.shape[0]):
     *         raise ValueError('Histogram lengths must be equal')             # <<<<<<<<<<<<<<
     *
     *
     */
    __pyx_tuple__4 = PyTuple_Pack(1, __pyx_kp_u_Histogram_lengths_must_be_equal);
    if (unlikely(!__pyx_tuple__4))
        __PYX_ERR(0, 48, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__4);
    __Pyx_GIVEREF(__pyx_tuple__4);

    /* "pyemd/emd.pyx":206
     *     # Validate arrays
     *     if not (first_array.size > 0 and second_array.size > 0):
     *         raise ValueError('Arrays of samples cannot be empty.')             # <<<<<<<<<<<<<<
     *     # Get the default range
     *     if range is None:
     */
    __pyx_tuple__5 = PyTuple_Pack(1, __pyx_kp_u_Arrays_of_samples_cannot_be_empt);
    if (unlikely(!__pyx_tuple__5))
        __PYX_ERR(0, 206, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__5);
    __Pyx_GIVEREF(__pyx_tuple__5);

    /* "pyemd/emd.pyx":230
     *         second_histogram = second_histogram / np.sum(second_histogram)
     *     # Compute the distance matrix between the center of each bin
     *     bin_locations = np.mean([bin_edges[:-1], bin_edges[1:]], axis=0)             # <<<<<<<<<<<<<<
     *     if distance == 'euclidean':
     *         distance = euclidean_pairwise_distance_matrix
     */
    __pyx_slice__6 = PySlice_New(Py_None, __pyx_int_neg_1, Py_None);
    if (unlikely(!__pyx_slice__6))
        __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_slice__6);
    __Pyx_GIVEREF(__pyx_slice__6);
    __pyx_slice__7 = PySlice_New(__pyx_int_1, Py_None, Py_None);
    if (unlikely(!__pyx_slice__7))
        __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_slice__7);
    __Pyx_GIVEREF(__pyx_slice__7);

    /* "pyemd/emd.pyx":236
     *     # Validate distance matrix
     *     if len(distance_matrix) != len(distance_matrix[0]):
     *         raise ValueError(             # <<<<<<<<<<<<<<
     *             'Distance matrix must be square; check your `distance` function.')
     *     if (first_histogram.shape[0] > len(distance_matrix) or
     */
    __pyx_tuple__8 = PyTuple_Pack(1, __pyx_kp_u_Distance_matrix_must_be_square_c);
    if (unlikely(!__pyx_tuple__8))
        __PYX_ERR(0, 236, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__8);
    __Pyx_GIVEREF(__pyx_tuple__8);

    /* "pyemd/emd.pyx":240
     *     if (first_histogram.shape[0] > len(distance_matrix) or
     *         second_histogram.shape[0] > len(distance_matrix)):
     *         raise ValueError(             # <<<<<<<<<<<<<<
     *             'Distance matrix must have at least as many rows/columns as there '
     *             'are bins in the histograms; check your `distance` function.')
     */
    __pyx_tuple__9 = PyTuple_Pack(1, __pyx_kp_u_Distance_matrix_must_have_at_lea);
    if (unlikely(!__pyx_tuple__9))
        __PYX_ERR(0, 240, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__9);
    __Pyx_GIVEREF(__pyx_tuple__9);

    /* "pyemd/emd.pyx":41
     *
     *
     * def _validate_emd_input(first_histogram, second_histogram, distance_matrix):             # <<<<<<<<<<<<<<
     *     """Validate EMD input."""
     *     if (first_histogram.shape[0] > distance_matrix.shape[0] or
     */
    __pyx_tuple__12 = PyTuple_Pack(3, __pyx_n_s_first_histogram, __pyx_n_s_second_histogram, __pyx_n_s_distance_matrix);
    if (unlikely(!__pyx_tuple__12))
        __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__12);
    __Pyx_GIVEREF(__pyx_tuple__12);
    __pyx_codeobj__13 = (PyObject *)__Pyx_PyCode_New(3, 0, 0, 3, 0, CO_OPTIMIZED | CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__12, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_src_pyemd_emd_pyx, __pyx_n_s_validate_emd_input, 41, __pyx_empty_bytes);
    if (unlikely(!__pyx_codeobj__13))
        __PYX_ERR(0, 41, __pyx_L1_error)

    /* "pyemd/emd.pyx":51
     *
     *
     * def emd(np.ndarray[np.float64_t, ndim=1, mode="c"] first_histogram,             # <<<<<<<<<<<<<<
     *         np.ndarray[np.float64_t, ndim=1, mode="c"] second_histogram,
     *         np.ndarray[np.float64_t, ndim=2, mode="c"] distance_matrix,
     */
    __pyx_tuple__14 = PyTuple_Pack(4, __pyx_n_s_first_histogram, __pyx_n_s_second_histogram, __pyx_n_s_distance_matrix, __pyx_n_s_extra_mass_penalty);
    if (unlikely(!__pyx_tuple__14))
        __PYX_ERR(0, 51, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__14);
    __Pyx_GIVEREF(__pyx_tuple__14);
    __pyx_codeobj__15 = (PyObject *)__Pyx_PyCode_New(4, 0, 0, 4, 0, CO_OPTIMIZED | CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__14, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_src_pyemd_emd_pyx, __pyx_n_s_emd, 51, __pyx_empty_bytes);
    if (unlikely(!__pyx_codeobj__15))
        __PYX_ERR(0, 51, __pyx_L1_error)

    /* "pyemd/emd.pyx":94
     *
     *
     * def emd_with_flow(np.ndarray[np.float64_t, ndim=1, mode="c"] first_histogram,             # <<<<<<<<<<<<<<
     *                   np.ndarray[np.float64_t, ndim=1, mode="c"] second_histogram,
     *                   np.ndarray[np.float64_t, ndim=2, mode="c"] distance_matrix,
     */
    __pyx_codeobj__16 = (PyObject *)__Pyx_PyCode_New(4, 0, 0, 4, 0, CO_OPTIMIZED | CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__14, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_src_pyemd_emd_pyx, __pyx_n_s_emd_with_flow, 94, __pyx_empty_bytes);
    if (unlikely(!__pyx_codeobj__16))
        __PYX_ERR(0, 94, __pyx_L1_error)

    /* "pyemd/emd.pyx":138
     *
     *
     * def euclidean_pairwise_distance_matrix(x):             # <<<<<<<<<<<<<<
     *     """Calculate the Euclidean pairwise distance matrix for a 1D array."""
     *     distance_matrix = np.abs(np.repeat(x, len(x)) - np.tile(x, len(x)))
     */
    __pyx_tuple__17 = PyTuple_Pack(2, __pyx_n_s_x, __pyx_n_s_distance_matrix);
    if (unlikely(!__pyx_tuple__17))
        __PYX_ERR(0, 138, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__17);
    __Pyx_GIVEREF(__pyx_tuple__17);
    __pyx_codeobj__18 = (PyObject *)__Pyx_PyCode_New(1, 0, 0, 2, 0, CO_OPTIMIZED | CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__17, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_src_pyemd_emd_pyx, __pyx_n_s_euclidean_pairwise_distance_matr, 138, __pyx_empty_bytes);
    if (unlikely(!__pyx_codeobj__18))
        __PYX_ERR(0, 138, __pyx_L1_error)

    /* "pyemd/emd.pyx":145
     *
     * # Use `np.histogram_bin_edges` if available (since NumPy version 1.15.0)
     * if parse_version(np.__version__) >= parse_version('1.15.0'):             # <<<<<<<<<<<<<<
     *     get_bins = np.histogram_bin_edges
     * else:
     */
    __pyx_tuple__19 = PyTuple_Pack(1, __pyx_kp_u_1_15_0);
    if (unlikely(!__pyx_tuple__19))
        __PYX_ERR(0, 145, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__19);
    __Pyx_GIVEREF(__pyx_tuple__19);

    /* "pyemd/emd.pyx":148
     *     get_bins = np.histogram_bin_edges
     * else:
     *     def get_bins(a, bins=10, **kwargs):             # <<<<<<<<<<<<<<
     *         if isinstance(bins, str):
     *             hist, bins = np.histogram(a, bins=bins, **kwargs)
     */
    __pyx_tuple__20 = PyTuple_Pack(4, __pyx_n_s_a, __pyx_n_s_bins, __pyx_n_s_kwargs, __pyx_n_s_hist);
    if (unlikely(!__pyx_tuple__20))
        __PYX_ERR(0, 148, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__20);
    __Pyx_GIVEREF(__pyx_tuple__20);
    __pyx_codeobj__21 = (PyObject *)__Pyx_PyCode_New(2, 0, 0, 4, 0, CO_OPTIMIZED | CO_NEWLOCALS | CO_VARKEYWORDS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__20, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_src_pyemd_emd_pyx, __pyx_n_s_get_bins, 148, __pyx_empty_bytes);
    if (unlikely(!__pyx_codeobj__21))
        __PYX_ERR(0, 148, __pyx_L1_error)
    __pyx_tuple__22 = PyTuple_Pack(1, ((PyObject *)__pyx_int_10));
    if (unlikely(!__pyx_tuple__22))
        __PYX_ERR(0, 148, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__22);
    __Pyx_GIVEREF(__pyx_tuple__22);

    /* "pyemd/emd.pyx":154
     *
     *
     * def emd_samples(first_array,             # <<<<<<<<<<<<<<
     *                 second_array,
     *                 extra_mass_penalty=DEFAULT_EXTRA_MASS_PENALTY,
     */
    __pyx_tuple__24 = PyTuple_Pack(13, __pyx_n_s_first_array, __pyx_n_s_second_array, __pyx_n_s_extra_mass_penalty, __pyx_n_s_distance, __pyx_n_s_normalized, __pyx_n_s_bins, __pyx_n_s_range, __pyx_n_s_first_histogram, __pyx_n_s_bin_edges, __pyx_n_s_second_histogram, __pyx_n_s__23, __pyx_n_s_bin_locations, __pyx_n_s_distance_matrix);
    if (unlikely(!__pyx_tuple__24))
        __PYX_ERR(0, 154, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_tuple__24);
    __Pyx_GIVEREF(__pyx_tuple__24);
    __pyx_codeobj__25 = (PyObject *)__Pyx_PyCode_New(7, 0, 0, 13, 0, CO_OPTIMIZED | CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__24, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_src_pyemd_emd_pyx, __pyx_n_s_emd_samples, 154, __pyx_empty_bytes);
    if (unlikely(!__pyx_codeobj__25))
        __PYX_ERR(0, 154, __pyx_L1_error)
    __Pyx_RefNannyFinishContext();
    return 0;
__pyx_L1_error:;
    __Pyx_RefNannyFinishContext();
    return -1;
}
/* #### Code section: init_constants ### */

static CYTHON_SMALL_CODE int __Pyx_InitConstants(void)
{
    if (__Pyx_CreateStringTabAndInitStrings() < 0)
        __PYX_ERR(0, 1, __pyx_L1_error);
    __pyx_float_neg_1_0 = PyFloat_FromDouble(-1.0);
    if (unlikely(!__pyx_float_neg_1_0))
        __PYX_ERR(0, 1, __pyx_L1_error)
    __pyx_int_0 = PyInt_FromLong(0);
    if (unlikely(!__pyx_int_0))
        __PYX_ERR(0, 1, __pyx_L1_error)
    __pyx_int_1 = PyInt_FromLong(1);
    if (unlikely(!__pyx_int_1))
        __PYX_ERR(0, 1, __pyx_L1_error)
    __pyx_int_10 = PyInt_FromLong(10);
    if (unlikely(!__pyx_int_10))
        __PYX_ERR(0, 1, __pyx_L1_error)
    __pyx_int_neg_1 = PyInt_FromLong(-1);
    if (unlikely(!__pyx_int_neg_1))
        __PYX_ERR(0, 1, __pyx_L1_error)
    return 0;
__pyx_L1_error:;
    return -1;
}
/* #### Code section: init_globals ### */

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void)
{
    /* NumpyImportArray.init */
    /*
     * Cython has automatically inserted a call to _import_array since
     * you didn't include one when you cimported numpy. To disable this
     * add the line
     *   <void>numpy._import_array
     */
#ifdef NPY_FEATURE_VERSION
#ifndef NO_IMPORT_ARRAY
    if (unlikely(_import_array() == -1))
    {
        PyErr_SetString(PyExc_ImportError, "numpy.core.multiarray failed to import "
                                           "(auto-generated because you didn't call 'numpy.import_array()' after cimporting numpy; "
                                           "use '<void>numpy._import_array' to disable if you are certain you don't need it).");
    }
#endif
#endif

    if (unlikely(PyErr_Occurred()))
        __PYX_ERR(0, 1, __pyx_L1_error)

    return 0;
__pyx_L1_error:;
    return -1;
}
/* #### Code section: init_module ### */

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void);     /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void);       /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void);     /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void)
{
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
    /*--- Global init code ---*/
    __Pyx_RefNannyFinishContext();
    return 0;
}

static int __Pyx_modinit_variable_export_code(void)
{
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
    /*--- Variable export code ---*/
    __Pyx_RefNannyFinishContext();
    return 0;
}

static int __Pyx_modinit_function_export_code(void)
{
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
    /*--- Function export code ---*/
    __Pyx_RefNannyFinishContext();
    return 0;
}

static int __Pyx_modinit_type_init_code(void)
{
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
    /*--- Type init code ---*/
    __Pyx_RefNannyFinishContext();
    return 0;
}

static int __Pyx_modinit_type_import_code(void)
{
    __Pyx_RefNannyDeclarations PyObject *__pyx_t_1 = NULL;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
    /*--- Type import code ---*/
    __pyx_t_1 = PyImport_ImportModule(__Pyx_BUILTIN_MODULE_NAME);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(3, 9, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_ptype_7cpython_4type_type = __Pyx_ImportType_3_0_10(__pyx_t_1, __Pyx_BUILTIN_MODULE_NAME, "type",
#if defined(PYPY_VERSION_NUM) && PYPY_VERSION_NUM < 0x050B0000
                                                              sizeof(PyTypeObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyTypeObject),
#elif CYTHON_COMPILING_IN_LIMITED_API
                                                              sizeof(PyTypeObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyTypeObject),
#else
                                                              sizeof(PyHeapTypeObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyHeapTypeObject),
#endif
                                                              __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_7cpython_4type_type)
        __PYX_ERR(3, 9, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __pyx_t_1 = PyImport_ImportModule("numpy");
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(2, 202, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_ptype_5numpy_dtype = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "dtype", sizeof(PyArray_Descr), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyArray_Descr), __Pyx_ImportType_CheckSize_Ignore_3_0_10);
    if (!__pyx_ptype_5numpy_dtype)
        __PYX_ERR(2, 202, __pyx_L1_error)
    __pyx_ptype_5numpy_flatiter = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "flatiter", sizeof(PyArrayIterObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyArrayIterObject), __Pyx_ImportType_CheckSize_Ignore_3_0_10);
    if (!__pyx_ptype_5numpy_flatiter)
        __PYX_ERR(2, 225, __pyx_L1_error)
    __pyx_ptype_5numpy_broadcast = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "broadcast", sizeof(PyArrayMultiIterObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyArrayMultiIterObject), __Pyx_ImportType_CheckSize_Ignore_3_0_10);
    if (!__pyx_ptype_5numpy_broadcast)
        __PYX_ERR(2, 229, __pyx_L1_error)
    __pyx_ptype_5numpy_ndarray = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "ndarray", sizeof(PyArrayObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyArrayObject), __Pyx_ImportType_CheckSize_Ignore_3_0_10);
    if (!__pyx_ptype_5numpy_ndarray)
        __PYX_ERR(2, 238, __pyx_L1_error)
    __pyx_ptype_5numpy_generic = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "generic", sizeof(PyObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyObject), __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_5numpy_generic)
        __PYX_ERR(2, 809, __pyx_L1_error)
    __pyx_ptype_5numpy_number = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "number", sizeof(PyObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyObject), __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_5numpy_number)
        __PYX_ERR(2, 811, __pyx_L1_error)
    __pyx_ptype_5numpy_integer = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "integer", sizeof(PyObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyObject), __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_5numpy_integer)
        __PYX_ERR(2, 813, __pyx_L1_error)
    __pyx_ptype_5numpy_signedinteger = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "signedinteger", sizeof(PyObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyObject), __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_5numpy_signedinteger)
        __PYX_ERR(2, 815, __pyx_L1_error)
    __pyx_ptype_5numpy_unsignedinteger = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "unsignedinteger", sizeof(PyObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyObject), __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_5numpy_unsignedinteger)
        __PYX_ERR(2, 817, __pyx_L1_error)
    __pyx_ptype_5numpy_inexact = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "inexact", sizeof(PyObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyObject), __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_5numpy_inexact)
        __PYX_ERR(2, 819, __pyx_L1_error)
    __pyx_ptype_5numpy_floating = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "floating", sizeof(PyObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyObject), __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_5numpy_floating)
        __PYX_ERR(2, 821, __pyx_L1_error)
    __pyx_ptype_5numpy_complexfloating = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "complexfloating", sizeof(PyObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyObject), __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_5numpy_complexfloating)
        __PYX_ERR(2, 823, __pyx_L1_error)
    __pyx_ptype_5numpy_flexible = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "flexible", sizeof(PyObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyObject), __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_5numpy_flexible)
        __PYX_ERR(2, 825, __pyx_L1_error)
    __pyx_ptype_5numpy_character = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "character", sizeof(PyObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyObject), __Pyx_ImportType_CheckSize_Warn_3_0_10);
    if (!__pyx_ptype_5numpy_character)
        __PYX_ERR(2, 827, __pyx_L1_error)
    __pyx_ptype_5numpy_ufunc = __Pyx_ImportType_3_0_10(__pyx_t_1, "numpy", "ufunc", sizeof(PyUFuncObject), __PYX_GET_STRUCT_ALIGNMENT_3_0_10(PyUFuncObject), __Pyx_ImportType_CheckSize_Ignore_3_0_10);
    if (!__pyx_ptype_5numpy_ufunc)
        __PYX_ERR(2, 866, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_RefNannyFinishContext();
    return 0;
__pyx_L1_error:;
    __Pyx_XDECREF(__pyx_t_1);
    __Pyx_RefNannyFinishContext();
    return -1;
}

static int __Pyx_modinit_variable_import_code(void)
{
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
    /*--- Variable import code ---*/
    __Pyx_RefNannyFinishContext();
    return 0;
}

static int __Pyx_modinit_function_import_code(void)
{
    __Pyx_RefNannyDeclarations
        __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
    /*--- Function import code ---*/
    __Pyx_RefNannyFinishContext();
    return 0;
}

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject *__pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_emd(PyObject *module);                     /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
    {Py_mod_create, (void *)__pyx_pymod_create},
    {Py_mod_exec, (void *)__pyx_pymod_exec_emd},
    {0, NULL}};
#endif

#ifdef __cplusplus
namespace
{
    struct PyModuleDef __pyx_moduledef =
#else
static struct PyModuleDef __pyx_moduledef =
#endif
        {
            PyModuleDef_HEAD_INIT,
            "emd",
            0, /* m_doc */
#if CYTHON_PEP489_MULTI_PHASE_INIT
            0, /* m_size */
#elif CYTHON_USE_MODULE_STATE
        sizeof(__pyx_mstate), /* m_size */
#else
    -1, /* m_size */
#endif
            __pyx_methods /* m_methods */,
#if CYTHON_PEP489_MULTI_PHASE_INIT
            __pyx_moduledef_slots, /* m_slots */
#else
        NULL, /* m_reload */
#endif
#if CYTHON_USE_MODULE_STATE
            __pyx_m_traverse, /* m_traverse */
            __pyx_m_clear,    /* m_clear */
            NULL              /* m_free */
#else
        NULL, /* m_traverse */
        NULL, /* m_clear */
        NULL  /* m_free */
#endif
        };
#ifdef __cplusplus
} /* anonymous namespace */
#endif
#endif

#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif

#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initemd(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initemd(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_emd(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_emd(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
    return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void)
{
#if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1)
    {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    }
    else if (unlikely(main_interpreter_id != current_id))
#else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter)
    {
        main_interpreter = current_interpreter;
    }
    else if (unlikely(main_interpreter != current_interpreter))
#endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
#if CYTHON_COMPILING_IN_LIMITED_API
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *module, const char *from_name, const char *to_name, int allow_none)
#else
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char *from_name, const char *to_name, int allow_none)
#endif
{
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value))
    {
        if (allow_none || value != Py_None)
        {
#if CYTHON_COMPILING_IN_LIMITED_API
            result = PyModule_AddObject(module, to_name, value);
#else
            result = PyDict_SetItemString(moddict, to_name, value);
#endif
        }
        Py_DECREF(value);
    }
    else if (PyErr_ExceptionMatches(PyExc_AttributeError))
    {
        PyErr_Clear();
    }
    else
    {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject *__pyx_pymod_create(PyObject *spec, PyModuleDef *def)
{
    PyObject *module = NULL, *moddict, *modname;
    CYTHON_UNUSED_VAR(def);
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname))
        goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module))
        goto bad;
#if CYTHON_COMPILING_IN_LIMITED_API
    moddict = module;
#else
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict))
        goto bad;
#endif
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0))
        goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0))
        goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0))
        goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0))
        goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}

static CYTHON_SMALL_CODE int __pyx_pymod_exec_emd(PyObject *__pyx_pyinit_module)
#endif
#endif
{
    int stringtab_initialized = 0;
#if CYTHON_USE_MODULE_STATE
    int pystate_addmodule_run = 0;
#endif
    PyObject *__pyx_t_1 = NULL;
    PyObject *__pyx_t_2 = NULL;
    PyObject *__pyx_t_3 = NULL;
    PyObject *__pyx_t_4 = NULL;
    int __pyx_t_5;
    int __pyx_lineno = 0;
    const char *__pyx_filename = NULL;
    int __pyx_clineno = 0;
    __Pyx_RefNannyDeclarations
#if CYTHON_PEP489_MULTI_PHASE_INIT
        if (__pyx_m)
    {
        if (__pyx_m == __pyx_pyinit_module)
            return 0;
        PyErr_SetString(PyExc_RuntimeError, "Module 'emd' has already been imported. Re-initialisation is not supported.");
        return -1;
    }
#elif PY_MAJOR_VERSION >= 3
        if (__pyx_m) return __Pyx_NewRef(__pyx_m);
#endif
/*--- Module creation code ---*/
#if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_m = __pyx_pyinit_module;
    Py_INCREF(__pyx_m);
#else
#if PY_MAJOR_VERSION < 3
    __pyx_m = Py_InitModule4("emd", __pyx_methods, 0, 0, PYTHON_API_VERSION);
    Py_XINCREF(__pyx_m);
    if (unlikely(!__pyx_m))
        __PYX_ERR(0, 1, __pyx_L1_error)
#elif CYTHON_USE_MODULE_STATE
    __pyx_t_1 = PyModule_Create(&__pyx_moduledef);
    if (unlikely(!__pyx_t_1))
        __PYX_ERR(0, 1, __pyx_L1_error)
        {
            int add_module_result = PyState_AddModule(__pyx_t_1, &__pyx_moduledef);
            __pyx_t_1 = 0; /* transfer ownership from __pyx_t_1 to "emd" pseudovariable */
            if (unlikely((add_module_result < 0)))
                __PYX_ERR(0, 1, __pyx_L1_error)
            pystate_addmodule_run = 1;
        }
#else
    __pyx_m = PyModule_Create(&__pyx_moduledef);
    if (unlikely(!__pyx_m))
        __PYX_ERR(0, 1, __pyx_L1_error)
#endif
#endif
    CYTHON_UNUSED_VAR(__pyx_t_1);
    __pyx_d = PyModule_GetDict(__pyx_m);
    if (unlikely(!__pyx_d))
        __PYX_ERR(0, 1, __pyx_L1_error)
    Py_INCREF(__pyx_d);
    __pyx_b = __Pyx_PyImport_AddModuleRef(__Pyx_BUILTIN_MODULE_NAME);
    if (unlikely(!__pyx_b))
        __PYX_ERR(0, 1, __pyx_L1_error)
    __pyx_cython_runtime = __Pyx_PyImport_AddModuleRef((const char *)"cython_runtime");
    if (unlikely(!__pyx_cython_runtime))
        __PYX_ERR(0, 1, __pyx_L1_error)
    if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#if CYTHON_REFNANNY
    __Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
    if (!__Pyx_RefNanny)
    {
        PyErr_Clear();
        __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
        if (!__Pyx_RefNanny)
            Py_FatalError("failed to import 'refnanny' module");
    }
#endif
    __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_emd(void)", 0);
    if (__Pyx_check_binary_version(__PYX_LIMITED_VERSION_HEX, __Pyx_get_runtime_version(), CYTHON_COMPILING_IN_LIMITED_API) < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#ifdef __Pxy_PyFrame_Initialize_Offsets
    __Pxy_PyFrame_Initialize_Offsets();
#endif
    __pyx_empty_tuple = PyTuple_New(0);
    if (unlikely(!__pyx_empty_tuple))
        __PYX_ERR(0, 1, __pyx_L1_error)
    __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0);
    if (unlikely(!__pyx_empty_bytes))
        __PYX_ERR(0, 1, __pyx_L1_error)
    __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0);
    if (unlikely(!__pyx_empty_unicode))
        __PYX_ERR(0, 1, __pyx_L1_error)
#ifdef __Pyx_CyFunction_USED
    if (__pyx_CyFunction_init(__pyx_m) < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#endif
#ifdef __Pyx_FusedFunction_USED
    if (__pyx_FusedFunction_init(__pyx_m) < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#endif
#ifdef __Pyx_Coroutine_USED
    if (__pyx_Coroutine_init(__pyx_m) < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#endif
#ifdef __Pyx_Generator_USED
    if (__pyx_Generator_init(__pyx_m) < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#endif
#ifdef __Pyx_AsyncGen_USED
    if (__pyx_AsyncGen_init(__pyx_m) < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#endif
#ifdef __Pyx_StopAsyncIteration_USED
    if (__pyx_StopAsyncIteration_init(__pyx_m) < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#endif
/*--- Library function declarations ---*/
/*--- Threads initialization code ---*/
#if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
    PyEval_InitThreads();
#endif
    /*--- Initialize various global constants etc. ---*/
    if (__Pyx_InitConstants() < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
    stringtab_initialized = 1;
    if (__Pyx_InitGlobals() < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
    if (__Pyx_init_sys_getdefaultencoding_params() < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#endif
    if (__pyx_module_is_main_pyemd__emd)
    {
        if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0)
            __PYX_ERR(0, 1, __pyx_L1_error)
    }
#if PY_MAJOR_VERSION >= 3
    {
        PyObject *modules = PyImport_GetModuleDict();
        if (unlikely(!modules))
            __PYX_ERR(0, 1, __pyx_L1_error)
        if (!PyDict_GetItemString(modules, "pyemd.emd"))
        {
            if (unlikely((PyDict_SetItemString(modules, "pyemd.emd", __pyx_m) < 0)))
                __PYX_ERR(0, 1, __pyx_L1_error)
        }
    }
#endif
    /*--- Builtin init code ---*/
    if (__Pyx_InitCachedBuiltins() < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
    /*--- Constants init code ---*/
    if (__Pyx_InitCachedConstants() < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
    /*--- Global type/function init code ---*/
    (void)__Pyx_modinit_global_init_code();
    (void)__Pyx_modinit_variable_export_code();
    (void)__Pyx_modinit_function_export_code();
    (void)__Pyx_modinit_type_init_code();
    if (unlikely((__Pyx_modinit_type_import_code() < 0)))
        __PYX_ERR(0, 1, __pyx_L1_error)
    (void)__Pyx_modinit_variable_import_code();
    (void)__Pyx_modinit_function_import_code();
/*--- Execution code ---*/
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
    if (__Pyx_patch_abc() < 0)
        __PYX_ERR(0, 1, __pyx_L1_error)
#endif

    /* "pyemd/emd.pyx":6
     * # emd.pyx
     *
     * from pkg_resources import parse_version             # <<<<<<<<<<<<<<
     *
     * from libcpp.pair cimport pair
     */
    __pyx_t_2 = PyList_New(1);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 6, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_INCREF(__pyx_n_s_parse_version);
    __Pyx_GIVEREF(__pyx_n_s_parse_version);
    if (__Pyx_PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_parse_version))
        __PYX_ERR(0, 6, __pyx_L1_error);
    __pyx_t_3 = __Pyx_Import(__pyx_n_s_pkg_resources, __pyx_t_2, 0);
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 6, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_3, __pyx_n_s_parse_version);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 6, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_parse_version, __pyx_t_2) < 0)
        __PYX_ERR(0, 6, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3);
    __pyx_t_3 = 0;

    /* "pyemd/emd.pyx":13
     *
     * # Import both NumPy and the Cython declarations for NumPy
     * import numpy as np             # <<<<<<<<<<<<<<
     * cimport numpy as np
     *
     */
    __pyx_t_3 = __Pyx_ImportDottedModule(__pyx_n_s_numpy, NULL);
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 13, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_np, __pyx_t_3) < 0)
        __PYX_ERR(0, 13, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3);
    __pyx_t_3 = 0;

    /* "pyemd/emd.pyx":38
     * # ==============
     *
     * DEFAULT_EXTRA_MASS_PENALTY = -1.0             # <<<<<<<<<<<<<<
     *
     *
     */
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_DEFAULT_EXTRA_MASS_PENALTY, __pyx_float_neg_1_0) < 0)
        __PYX_ERR(0, 38, __pyx_L1_error)

    /* "pyemd/emd.pyx":41
     *
     *
     * def _validate_emd_input(first_histogram, second_histogram, distance_matrix):             # <<<<<<<<<<<<<<
     *     """Validate EMD input."""
     *     if (first_histogram.shape[0] > distance_matrix.shape[0] or
     */
    __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_5pyemd_3emd_1_validate_emd_input, 0, __pyx_n_s_validate_emd_input, NULL, __pyx_n_s_pyemd_emd, __pyx_d, ((PyObject *)__pyx_codeobj__13));
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_validate_emd_input, __pyx_t_3) < 0)
        __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3);
    __pyx_t_3 = 0;

    /* "pyemd/emd.pyx":51
     *
     *
     * def emd(np.ndarray[np.float64_t, ndim=1, mode="c"] first_histogram,             # <<<<<<<<<<<<<<
     *         np.ndarray[np.float64_t, ndim=1, mode="c"] second_histogram,
     *         np.ndarray[np.float64_t, ndim=2, mode="c"] distance_matrix,
     */
    __pyx_t_3 = __Pyx_CyFunction_New(&__pyx_mdef_5pyemd_3emd_3emd, 0, __pyx_n_s_emd, NULL, __pyx_n_s_pyemd_emd, __pyx_d, ((PyObject *)__pyx_codeobj__15));
    if (unlikely(!__pyx_t_3))
        __PYX_ERR(0, 51, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    if (!__Pyx_CyFunction_InitDefaults(__pyx_t_3, sizeof(__pyx_defaults), 1))
        __PYX_ERR(0, 51, __pyx_L1_error)

    /* "pyemd/emd.pyx":54
     *         np.ndarray[np.float64_t, ndim=1, mode="c"] second_histogram,
     *         np.ndarray[np.float64_t, ndim=2, mode="c"] distance_matrix,
     *         extra_mass_penalty=DEFAULT_EXTRA_MASS_PENALTY):             # <<<<<<<<<<<<<<
     *     u"""Return the EMD between two histograms using the given distance matrix.
     *
     */
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_DEFAULT_EXTRA_MASS_PENALTY);
    if (unlikely(!__pyx_t_2))
        __PYX_ERR(0, 54, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_CyFunction_Defaults(__pyx_defaults, __pyx_t_3)->__pyx_arg_extra_mass_penalty = __pyx_t_2;
    __Pyx_GIVEREF(__pyx_t_2);
    __pyx_t_2 = 0;
    __Pyx_CyFunction_SetDefaultsGetter(__pyx_t_3, __pyx_pf_5pyemd_3emd_12__defaults__);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_emd, __pyx_t_3) < 0)
        __PYX_ERR(0, 51, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3);
    __pyx_t_3 = 0;

    /* "pyemd/emd.pyx":94

