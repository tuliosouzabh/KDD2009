from sklearn.metrics import *
import numpy as np

class Metricas:
    
    @classmethod
    def smape(cls, A, F):
        return 100/len(A) * np.sum(2 * np.abs(F - A) / (np.abs(A) + np.abs(F)))
        
    @classmethod
    def calcular(cls, y_true, y_pred):
        resultados = {'mean_absolute_error': round(mean_absolute_error(y_true, y_pred),4),
                      'mean_squared_error': round(mean_squared_error(y_true, y_pred),4),
                      'r2': round(r2_score(y_true, y_pred),4),
                      'smape': round(cls.smape(y_true, y_pred),4)
                     }        
        return resultados
    
    
    @classmethod
    def calcular_classificacao(cls, y_true, y_pred, classes, normalize=False, title="Matriz de confusão"):
        resultados = {'matriz confusão': confusion_matrix(y_true, y_pred),
                      'acurácia': accuracy_score(y_true, y_pred),
                      'f1 score': f1_score(y_true, y_pred),
                      'precision': precision_score(y_true, y_pred),
                      'recall': recall_score(y_true, y_pred),
                      'roc auc': roc_auc_score(y_true, y_pred)
                     }        
        return resultados